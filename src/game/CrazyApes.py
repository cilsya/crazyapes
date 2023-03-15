# wxPython documentation
# https://wxpython.org/Phoenix/docs/html/wx.1moduleindex.html

#------------------------ Imports (Start) --------------------------------------

# Native modules

# Third-party modules
import wx

# Custom modules
import asset_data
import define_data
import drawEngine
import level
import level_data
import mage

#------------------------ Imports (End) ----------------------------------------

class ID_list(object):
    
    #-------------------------
    # Static Member Variables
    # (Start)
    #-------------------------
    
    ID_New = 400
    ID_Load = 401
    ID_About = 402
    ID_Exit = 403
    
    ID_Timer = 404
    
    #-------------------------
    # Static Member Variables
    # (End)
    #-------------------------

class CrazyApesFrame(wx.Frame):
    """
    https://wxpython.org/Phoenix/docs/html/wx.Frame.html
    """
    
    def __init__(self,parent, title):
        
        super(CrazyApesFrame, self).__init__( parent,
                                              title = title,
                                              pos = (100, 100),
                                              size = (650, 500) )
        
        #---------------------------
        # Game variables
        # (Start)
        #---------------------------
        
        ## TEMP
        ##
        #self.TEMP_on_paint_count = 0
        
        # https://wxpython.org/Phoenix/docs/html/wx.Timer.html
        self.timer = wx.Timer( self, 
                               ID_list.ID_Timer)
        
        #self.level = None
        #self.player = None
        self.drawArea = drawEngine.DrawEngine()
        
        # Back-buffer
        # wxBitmap
        # https://wxpython.org/Phoenix/docs/html/wx.Bitmap.html
        #
        # Draw everything onto the back buffer, when it is done, flip it onto
        # the screen. It prevents flickering.
        self.backBuffer = wx.Bitmap(
            define_data.LEVEL_X * define_data.GRID_SIZE,
            define_data.LEVEL_Y * define_data.GRID_SIZE )
        
        #---------------------------
        # Game variables
        # (End)
        #---------------------------
        
        # https://wxpython.org/Phoenix/docs/html/wx.StaticText.html
        self.stPlayerLives = None
        self.stCurrentLevel = None
        self.stNumberEnemies = None
        
        # https://wxpython.org/Phoenix/docs/html/wx.MenuBar.html
        self.menu_bar = wx.MenuBar()
        
        # https://wxpython.org/Phoenix/docs/html/wx.Menu.html
        self.menuFile = wx.Menu()
        
        # Populate menu file
        self.menuFile.Append(ID_list.ID_New, "&New")
        self.menuFile.AppendSeparator()
        self.menuFile.Append(ID_list.ID_Load, "&Load")
        self.menuFile.AppendSeparator()
        self.menuFile_about = self.menuFile.Append(ID_list.ID_About, "&About")
        self.menuFile.AppendSeparator()
        self.menuFile.Append(ID_list.ID_Exit, "E&xit")
        
        # Put menu file to the menu bar
        self.menu_bar.Append(self.menuFile, "&File")
        
        # Set the menu bar
        self.SetMenuBar(self.menu_bar)
        
        #https://wxpython.org/Phoenix/docs/html/wx.Panel.html
        self.panel = CrazyApesPanel(self)
        
        # Panel(parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize,
        # style=TAB_TRAVERSAL, name=PanelNameStr)
        self.info_panel = wx.Panel(self.panel, 
                                   wx.ID_ANY,
                                   wx.DefaultPosition,
                                   wx.Size(200, 400),
                                   wx.BORDER_STATIC)
        
        # https://wxpython.org/Phoenix/docs/html/wx.Window.html
        #
        # Window(parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize,
        # style=0, name=PanelNameStr)
        self.gameWindow = wx.Window(self.panel, 
                                    wx.ID_ANY,
                                    wx.DefaultPosition,
                                    wx.Size(200, 200),
                                    wx.BORDER_STATIC)
        
        # Connect the game window to the paint event.
        # https://wxpython.org/Phoenix/docs/html/
        # wx.EvtHandler.html#wx.EvtHandler.Connect
        #self.gameWindow.Connect( -1,
        #                        -1,
        #                        wx.EVT_PAINT,
        #                        self.OnPaint )
        
        # StaticText(parent, id=ID_ANY, label="", pos=DefaultPosition,
        #  size=DefaultSize, style=0, name=StaticTextNameStr)
        self.stPlayerLives = wx.StaticText( self.info_panel,
                                            wx.ID_ANY,
                                            "Lives:",
                                            wx.DefaultPosition,
                                            wx.Size(100, 15),
                                            wx.ST_NO_AUTORESIZE  )
        
        self.stCurrentLevel = wx.StaticText( self.info_panel,
                                            wx.ID_ANY,
                                            "Level:",
                                            wx.DefaultPosition,
                                            wx.Size(100, 15),
                                            wx.ST_NO_AUTORESIZE  )
        
        self.stNumberEnemies = wx.StaticText( self.info_panel,
                                              wx.ID_ANY,
                                              "Enemies:",
                                              wx.DefaultPosition,
                                              wx.Size(100, 15),
                                              wx.ST_NO_AUTORESIZE  )
        
        # Layout
        # https://wxpython.org/Phoenix/docs/html/wx.BoxSizer.html
        self.mainsizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Inherited from wx.Sizer
        # https://wxpython.org/Phoenix/docs/html/wx.Sizer.html#wx.Sizer.Add
        self.mainsizer.Add(self.gameWindow, 
                           1,
                           wx.GROW|wx.ALL,
                           5 )
        self.mainsizer.Add(self.info_panel, 
                           0,
                           wx.GROW|wx.ALL|wx.STRETCH_NOT,
                           5 )
        
        self.subsizer = wx.BoxSizer(wx.VERTICAL)
        self.subsizer.Add(self.stPlayerLives, 
                     0,
                     wx.LEFT|wx.TOP,
                     5 )
        self.subsizer.Add(self.stCurrentLevel, 
                     0,
                     wx.LEFT|wx.TOP,
                     5 )
        self.subsizer.Add(self.stNumberEnemies, 
                     0,
                     wx.LEFT|wx.TOP,
                     5 )
        
        # Set the layout (sizer) that we have created
        self.panel.SetAutoLayout(True)
        self.panel.SetSizer(self.mainsizer)
        #
        self.info_panel.SetAutoLayout(True)
        self.info_panel.SetSizer(self.subsizer)
        
        #-------------------------
        # Draw Tiles
        # (Start)
        #-------------------------
        
        # Empty Tile
        self.drawArea.createBackgroundTile(
            
            # Index
            level_data.Enum.TILE_EMPTY,
            
            # wxBitmap
            wx.Bitmap(asset_data.EmptyTile))
        
        # Wall Tile
        self.drawArea.createBackgroundTile(
            
            # Index
            level_data.Enum.TILE_WALL,
            
            # wxBitmap
            wx.Bitmap(asset_data.WallTile))
        
        #---------------------------------
        
        # Sprite player
        self.drawArea.createSprite(
            
            # Index
            level_data.Enum_Entity.SPRITE_PLAYER,
            
            # wxBitmap
            wx.Bitmap(asset_data.PlayerTile))
        
        # Sprite enemy
        self.drawArea.createSprite(
            
            # Index
            level_data.Enum_Entity.SPRITE_ENEMY,
            
            # wxBitmap
            wx.Bitmap(asset_data.EnemyTile))
        
        # Sprite fireball
        self.drawArea.createSprite(
            
            # Index
            level_data.Enum_Entity.SPRITE_FIREBALL,
            
            # wxBitmap
            wx.Bitmap(asset_data.FireballTile))
        
        #-------------------------
        # Draw Tiles
        # (End)
        #-------------------------
        
        # Set the member variables for the draw engine
        self.drawArea.setWindow( self.backBuffer,
                                 define_data.LEVEL_X,
                                 define_data.LEVEL_Y)
        
        # Start the timer
        # Pass it a number in milliseconds between delay
        self.timer.Start(define_data.UPDATE_TIME)
        
        # Create a new lvel
        self.level = level.Level( self.drawArea,
                                  define_data.LEVEL_X,
                                  define_data.LEVEL_Y)
        
        # Create a new player
        self.player = mage.Mage( self.level,
                                 self.drawArea,
                                 0)
        
        
        # Draw level
        # NOTE: Just by calling this, the user won't see anything.
        #       The reason is this is calling the self.drawArea (which is
        #       a draw engine) and it is drawing to the backbuffer.
        self.level.draw()
        #
        # Add player
        self.level.addPlayer(self.player)
        #
        # Add enemies
        self.level.addEnemies(3)
        
        # NEW METHOD CREATED, update backend code
        self.level.setPlayerStart()
        
        # Update the level so everything gets initialized
        self.level.update()
        
        
        # Bind call backs to menu objects
        #self.menuFile.Bind(wx.EVT_MENU, self.OnAbout)
        
        # Bind action to menu : menu wxPython Python Tutorial
        #
        # http://www.java2s.com/Tutorial/Python/
        # 0380__wxPython/Bindactiontomenu.htm
        self.Bind(wx.EVT_MENU, self.OnAbout, self.menuFile_about)
        
        # Paint event in wxPython
        #self.Bind(wx.EVT_PAINT,
        #        self.OnPaint,
        #        self.gameWindow)
        
        ## Paint event in wxPython
        #self.Bind(wx.EVT_PAINT,
        #          self.OnPaint)
        
        # Bind paint event to game window
        self.gameWindow.Bind(wx.EVT_PAINT,
                             self.OnPaint)
        
        # Bind timer event to wxTimer object
        self.Bind(wx.EVT_TIMER, 
                  self.OnTimer)
        
        # Connect keyboard event
        self.gameWindow.Bind(wx.EVT_KEY_DOWN,
                             self.OnKey)
        
    def OnNew(self, event):
        pass
    
    def OnLoad(self, event):
        pass
    
    def OnAbout(self, event):
        
        # https://wxpython.org/Phoenix/docs/html/wx.functions.html#wx.MessageBox
        wx.MessageBox("The Crazy Apes game. Can you survive?",
                      "About Crazy Apes")
        
        ## DEBUG
        ##
        ## wxPython not binding callbacks to events properly
        ##
        ## https://stackoverflow.com/questions/4242147/
        ## wxpython-not-binding-callbacks-to-events-properly/4242889#4242889
        #print("DEBUG - Menu Item Selected: {}".format(
        #        self.menuFile.FindItemById(event.Id).Label) )
    
    def OnExit(self, event):
        pass
    
    def OnPaint(self, event):
        
        ## DEBUG
        ##
        #self.TEMP_on_paint_count += 1
        #text = "Number of paint events: {0}".format(self.TEMP_on_paint_count)
        #print("DEBUG - {}".format(text))

        
        
        ## DEBUG
        ##
        #print("DEBUG - We entered the wx paint event")
        
        # https://wxpython.org/Phoenix/docs/html/wx.PaintDC.html
        #
        # IMPORTANT:
        # - don't store a wx.PaintDC object. 
        # - If you have an EVT_PAINT() handler, 
        #   you must create a wx.PaintDC object within it even if 
        #   you don't actually use it.
        dc = wx.PaintDC(self.gameWindow)
        #dc = wx.PaintDC(self)
        
        # Set to a black brush
        dc.SetBackground(wx.BLACK_BRUSH)
        
        # Must clear so the device context will clear it to black.
        # NOTE: Just because you set the background does not mean it will
        #       clear it automatically
        dc.Clear()
        
        # Now draw the bitmap FROM the backbuffer (because that
        # is where all of the game is being drawn, to the top left corner
        dc.DrawBitmap( self.backBuffer,
                      wx.Point(0,0) )
        
    def OnTimer(self, event):
        
        # Update the level
        self.level.update()
        
        # Update the viewing area
        #----------------------------------
        
        # Cannot use a wxPaintDC, must use a wxClientDC when it is outside
        # an onPaint event handler
        #
        # https://wxpython.org/Phoenix/docs/html/wx.ClientDC.html
        area = wx.ClientDC(self.gameWindow)
        
        area.DrawBitmap( self.backBuffer,
                         wx.Point(0,0) )
        
    def OnKey(self, event):
        
        # Only 1 bit difference between a lower-case character and a 
        # upper case character by "OR"'ing it (using "|") we ensure that 
        # 1 bit is always 1.
        # It will always ensure it is lower case.
        #self.keyPress(event.GetKeyCode() | 32)
        #
        result = event.GetKeyCode()
        #
        # Always get lower case
        result_bit = result | 32
        #
        # Convert ascii code to letter
        result_letter = chr(result)
        #
        # Convert to lower case
        result_letter_bit = chr(result_bit)
        #
        self.level.keyPress(result_letter_bit)
        
        ## DEBUG
        ##
        #print("DEBUG - OnKey callback. event.GetKeyCode(): {}".format(result))
        #print("DEBUG - OnKey callback. event.GetKeyCode() with bit: {}".format(
        #                                                            result_bit))
        #print("DEBUG - OnKey callback. letter: {}".format(result_letter))
        #print("DEBUG - OnKey callback. result_letter_bit with bit: {}".format(
        #                                                    result_letter_bit))
        # Update the viewing area
        #----------------------------------
        
        # Cannot use a wxPaintDC, must use a wxClientDC when it is outside
        # an onPaint event handler
        #
        # https://wxpython.org/Phoenix/docs/html/wx.ClientDC.html
        area = wx.ClientDC(self.gameWindow)
        
        area.DrawBitmap( self.backBuffer,
                         wx.Point(0,0) )
        
class CrazyApesPanel(wx.Panel):
    """
    Description: This is the panel that goes into the main apps frame.
    """
    
    def __init__( self,
                  parent ):
        super(CrazyApesPanel, self).__init__(parent)
        
class CrazyApesApp(wx.App):
    """
    Description: This is the main app.
    """
    
    def OnInit(self):
        
        # Create the main window
        self.frame = CrazyApesFrame( parent = None,
                                     title = "Crazy Apes")
        
        # Show the main window
        self.frame.Show()
        
        return True
        
#--------------------------- Auto-Execute (Start) ------------------------------

if __name__ == "__main__":
    
    app = CrazyApesApp()
    app.MainLoop()
    
#--------------------------- Auto-Execute (End) --------------------------------