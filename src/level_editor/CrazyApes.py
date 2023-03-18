# wxPython documentation
# https://wxpython.org/Phoenix/docs/html/wx.1moduleindex.html

#------------------------ Imports (Start) --------------------------------------

# Native modules
import math
import pickle
import time
import sys

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
    
class LevelType(object):
    
    #-------------------------
    # Static Member Variables
    # (Start)
    #-------------------------
    
    RANDOM_NEW_LEVEL = 0
    NEXT_PACKAGE_LEVEL = 1
    
    #-------------------------
    # Static Member Variables
    # (End)
    #-------------------------
    
class Level_Info:
    def __init__(self):
        self.grid_x = None
        self.grid_y = None
        self.grid = None

class CrazyApesFrame(wx.Frame):
    """
    https://wxpython.org/Phoenix/docs/html/wx.Frame.html
    """
    
    def __init__( self,
                  parent,
                  title,
                  pos = (100, 100),
                  size = (900, 500),
                  filename = "",
                  startingLevel = 0 ):
        
        super(CrazyApesFrame, self).__init__( parent,
                                              title = title,
                                              pos = pos,
                                              size = size )
        
        #---------------------------
        # Game variables
        # (Start)
        #---------------------------
        
        ## TEMP
        ##
        #self.TEMP_on_paint_count = 0
        
        self.currentLevel = None
        self.gameState = None
        self.backBuffer = None
        self.finalBackBuffer = None
        
        self.package = []
        self.packageLoaded = False
        
        # https://wxpython.org/Phoenix/docs/html/wx.Timer.html
        self.timer = wx.Timer( self, 
                               ID_list.ID_Timer)
        
        self.level = None
        self.player = None
        self.drawArea = drawEngine.DrawEngine()
        
        # Elapsed time values
        self.time_initial = 0.0
        
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
        self.menuFile_new = self.menuFile.Append(ID_list.ID_New, "&New")
        self.menuFile.AppendSeparator()
        self.menuFile_load = self.menuFile.Append(ID_list.ID_Load, "&Load")
        self.menuFile.AppendSeparator()
        self.menuFile_about = self.menuFile_about = self.menuFile.Append(
                                                ID_list.ID_About, "&About")
        self.menuFile.AppendSeparator()
        self.menuFile_exit = self.menuFile_exit = self.menuFile.Append(
                                                   ID_list.ID_Exit, "E&xit")
        
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
        
        # Start the timer
        # Pass it a number in milliseconds between delay
        self.timer.Start(define_data.UPDATE_TIME)
        
        self.gameState = level_data.Enum_GameState.STATE_NULL
        
        if filename != "":
            self.loadGame(filename,
                          startingLevel)
        
        #-----------------------------------------
        # Bind Callbacks
        # (Start)
        #-----------------------------------------
        
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
        
        # Bind paint event to game window
        self.gameWindow.Bind(wx.EVT_SIZE,
                             self.OnSize)
        
        # Bind timer event to wxTimer object
        self.Bind(wx.EVT_TIMER, 
                  self.OnTimer)
        
        # Connect keyboard event
        self.gameWindow.Bind(wx.EVT_KEY_DOWN,
                             self.OnKey)
        
        # Selecting new menu item
        self.Bind(wx.EVT_MENU,
                  self.OnNew,
                  self.menuFile_new)
        
        # Callback - Load
        self.Bind( wx.EVT_MENU,
                   self.OnLoad,
                   self.menuFile_load )
        
        # Selecting exit menu item
        self.Bind(wx.EVT_MENU,
                  self.OnExit,
                  self.menuFile_exit)
        
        
        #-----------------------------------------
        # Bind Callbacks
        # (End)
        #-----------------------------------------
        
    def __del__(self):
        
        # This is no game
        self.gameState = level_data.Enum_GameState.STATE_NULL
        self.timer.Stop()
        self.timer=None
        
        # delete self.player
        # delete self.level
        
    def OnNew(self, event):
        
        self.timer.Stop()
        
        # Get rid of player object if one exists
        if self.player is not None:
            self.player = None
        
        # Create a new player
        self.player = mage.Mage( self.level,
                                 self.drawArea,
                                 0)
        
        # Create RANDOM new level
        self.startNewLevel( LevelType.RANDOM_NEW_LEVEL )
        
        # Draw level
        # NOTE: Just by calling this, the user won't see anything.
        #       The reason is this is calling the self.drawArea (which is
        #       a draw engine) and it is drawing to the backbuffer.
        #self.level.draw()

        # Add enemies
        self.level.addEnemies(1, 5)
        
        self.level.setPlayerStart()
        
        # Set the level to 1.
        # It is the first level because it is a new game.
        self.currentLevel = 1
        
        self.gameState = level_data.Enum_GameState.STATE_GAME_IN_PROGRESS
        
        self.timer.Start(define_data.UPDATE_TIME)
        
    def OnLoad(self, event):
        
        # https://wxpython.org/Phoenix/docs/html/wx.FileDialog.html
        dialog = wx.FileDialog( self,
                                "Open Package",
                                "",
                                "",
                                "Package (*.pkg)|*.pkg",
                                wx.FD_OPEN )
        
        if dialog.ShowModal() == wx.ID_OK:
            
            self.loadGame( dialog.GetPath() )
    
    def loadGame(self,
                 filename,
                 startingLevel = 1):
        
        self.package = []
        
        # Create a new player
        self.player = mage.Mage( None,
                                 self.drawArea,
                                 0)
        
        with open(filename, "rb") as handle:
            data = pickle.load(handle)
        
        # We are going to update the internal data
        # BUT FIRST
        # We populate local variables in case something fails
        package = []
        numLevels = len(data)
        firstLevel = None
        
        for i in range(numLevels):
            
            level_temp = Level_Info()
            level_temp.grid = data[i]
            level_temp.grid_x = len(level_temp.grid)
            level_temp.grid_y = len(level_temp.grid[0])
            
            package.append(level_temp)
            
            if i == startingLevel - 1:
                
                self.currentLevel = startingLevel
                firstLevel = level_temp
                
            ## Now we update the internal data
            #self.package = package
            #self.levelIndex = 1
            #self.setCurrentLevel(self.package[0])
            
            
        # Set member variable package
        self.package = package
        
        self.packageLoaded = True
        
        self.startNewLevel( LevelType.NEXT_PACKAGE_LEVEL )
        
        self.level.addEnemies(0)
        self.currentLevel = 1
        
        self.gameState = level_data.Enum_GameState.STATE_GAME_IN_PROGRESS
        
        # Start the timer
        # Pass it a number in milliseconds between delay
        self.timer.Start(define_data.UPDATE_TIME)
        
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
        self.Close(True)
    
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
        
        self.updateView()
        
    def OnTimer(self, event):
                                        
        if self.gameState == level_data.Enum_GameState.STATE_GAME_IN_PROGRESS:
            self.updateGame()
        
    def OnKey(self, event):
        
        if self.gameState == level_data.Enum_GameState.STATE_GAME_IN_PROGRESS:
        
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
        
        # Now update the view
        self.updateView()
        
    def OnSize(self, event):
        
        # https://docs.wxpython.org/wx.Event.html?highlight=skip#wx.Event.Skip
        #
        # Basically saying do you normally do to automatically handle certain
        # things in the event, then give us control before returning.
        event.Skip()
        
        # Delete finalBackBuffer if it already exists
        if self.finalBackBuffer is not None:
            self.finalBackBuffer = None
            
        clientArea = self.gameWindow.GetClientSize()
        
        self.finalBackBuffer = wx.Bitmap(clientArea.GetWidth(),
                                         clientArea.GetHeight())
        
        self.updateView()
        
    def startNewLevel( self,
                       type):
    
        # Delete level if it already exists
        if self.level is not None:
            self.level = None
        
        if self.backBuffer is not None:
            self.backBuffer = None
        
        if type == LevelType.RANDOM_NEW_LEVEL:
            
            # Create a new level
            self.level = level.Level( self.drawArea,
                                      define_data.LEVEL_X,
                                      define_data.LEVEL_Y)
            
        if type == LevelType.NEXT_PACKAGE_LEVEL:
            
            numLevels = len(self.package)
            
            if self.currentLevel > numLevels:
                return True
            
            for i in range(numLevels):
                
                if i == self.currentLevel -1:
                    
                    new_level = self.package[i]
                    
                    # Mimicking constructor overload
                    self.level = level.Level.init2( self.drawArea,
                                                    new_level.grid,
                                                    new_level.grid_x,
                                                    new_level.grid_y )
                    
                    # Break out of the loop
                    break

        # Back-buffer
        # wxBitmap
        # https://wxpython.org/Phoenix/docs/html/wx.Bitmap.html
        #
        # Draw everything onto the back buffer, when it is done, flip it onto
        # the screen. It prevents flickering.
        self.backBuffer = wx.Bitmap(
            self.level.getWidth() * define_data.GRID_SIZE,
            self.level.getHeight() * define_data.GRID_SIZE )
        
        # Set the member variables for the draw engine
        self.drawArea.setWindow( self.backBuffer,
                                 self.level.getWidth(),
                                 self.level.getHeight())
        
        # Add player
        self.level.addPlayer(self.player)
        
        # Draw level
        # NOTE: Just by calling this, the user won't see anything.
        #       The reason is this is calling the self.drawArea (which is
        #       a draw engine) and it is drawing to the backbuffer.
        self.level.draw()
        
        self.player.setLevel(self.level)
        #player.update()
        
        # NEW METHOD CREATED, update backend code
        self.level.setPlayerStart()
                                                             
        return True
    
    def updateView(self):
        
        # Cannot use a wxPaintDC, must use a wxClientDC when it is outside
        # an onPaint event handler
        #
        # https://wxpython.org/Phoenix/docs/html/wx.ClientDC.html
        area = wx.ClientDC(self.gameWindow)
        
        # Do not try to draw if there are no backbuffer
        if ( self.backBuffer is not None 
             and 
             self.gameState == \
             level_data.Enum_GameState.STATE_GAME_IN_PROGRESS ):
            
            # Update the viewing area
            #----------------------------------
            
            ## Cannot use a wxPaintDC, must use a wxClientDC when it is outside
            ## an onPaint event handler
            ##
            ## https://wxpython.org/Phoenix/docs/html/wx.ClientDC.html
            #area = wx.ClientDC(self.gameWindow)
            
            #area.DrawBitmap( self.backBuffer,
            #                 wx.Point(0,0) )
            
            self.stretchGameView()
            
        elif self.finalBackBuffer is not None:
            self.drawInformation()
        
        self.flipBackBuffer()
    
    def updateGame(self):
        
        ## DEBUG
        ##
        #print("DEBUG - updateGame callback")
        
        # Update GUI display
        info_Lives = "Lives: " + str(self.player.getLives())
        info_Level = "Level: " + str(self.currentLevel)
        info_NumEnemies = "Enemies: " + str(self.level.numEnemies())
    
        self.stPlayerLives.SetLabel(info_Lives)
        self.stCurrentLevel.SetLabel(info_Level)
        self.stNumberEnemies.SetLabel(info_NumEnemies)
        
        ## DEBUG
        ##
        #print("DEBUG - updateGame callback. numEnemies: {}".format(
        #                                   self.level.numEnemies()))
        
        # Check Game State
        if self.level.numEnemies() == 0:
            
            ## DEBUG
            ##
            #print("DEBUG - updateGame callback. No more enemies")
        
            self.timer.Stop()
            self.currentLevel += 1
            
            # Load level from package
            if self.packageLoaded == True:
                
                if self.startNewLevel(LevelType.NEXT_PACKAGE_LEVEL):
                
                    self.packageLoaded = False
                    self.gameState = level_data.Enum_GameState.STATE_PLAYER_WON
                    self.updateView()
                    
                    return
                    
                self.level.addEnemies(0)
                self.level.setPlayerStart()
            
            # If we did not load levels from a package, randomly create
            # a level.
            else:
            
                self.startNewLevel(LevelType.RANDOM_NEW_LEVEL)
            
                # Basic logic for enemies per level.
                # Level number multiplied by 4
                # Set to local variable
                numEnemies = self.currentLevel * 4
                
                # Cap max amount of enemies to 15
                if numEnemies > 15:
                    numEnemies = 15
                
                # Basic algorithm to make enemies faster
                newSpeed = math.pow(2, self.currentLevel)
                #
                # Clamp new speed
                if newSpeed > 100:
                    newSpeed = 100
                
                # Add enemies
                self.level.addEnemies(numEnemies, newSpeed)
                
                self.level.setPlayerStart()
            
            # Start the timer
            # Pass it a number in milliseconds between delay
            self.timer.Start(define_data.UPDATE_TIME)
            
        # What if the character dies
        elif self.level.numEnemies() > 0 and self.player.isAlive() == False:
            
            # If the game is over, set the package loaded to false
            self.packageLoaded = False
            
            ## DEBUG
            ##
            #print("DEBUG - updateGame callback. Game Over")
            
            # Game over state
            self.gameState = level_data.Enum_GameState.STATE_GAME_OVER
            
            # Stop the timer
            self.timer.Stop()
        else:
            
            ## DEBUG
            ##
            #print("DEBUG - updateGame callback. Playing Game.")
            
            # Measured in seconds, multiply by 1000.0
            # to make it milliseconds and type float
            time_elasped = self.get_elasped_time() * 1000.0
            
            ## DEBUG
            ##
            #print("DEBUG - self.updateGame() time_elasped: {}".format(
            #                                                    time_elasped))
            
            # Just update the level
            self.level.update(time_elasped)
            
        self.updateView()
        
    def start_timer(self):
        
        # https://docs.python.org/3/library/time.html#time.process_time
        # Measured in seconds (fractional seconds)
        self.time_initial = time.perf_counter()
        
    def get_elasped_time(self):
        return time.perf_counter() - self.time_initial
        
    def drawInformation(self):
        
        clientArea = self.gameWindow.GetClientSize()
        
        finalDC = wx.MemoryDC()
        
        finalDC.SelectObject(self.finalBackBuffer)
        
        finalDC.Clear()
        
        finalDC.DrawRectangle(0,
                              0,
                              clientArea.GetWidth(),
                              clientArea.GetHeight())
        
        message = ""
        
        if self.gameState == level_data.Enum_GameState.STATE_NULL:
            message = "Go to File > New to start a new game!"
        elif self.gameState == level_data.Enum_GameState.STATE_PLAYER_WON:
            message = "You have won the game!"
        elif self.gameState == level_data.Enum_GameState.STATE_GAME_OVER:
            message = "GAME OVER!"
        
        # https://docs.wxpython.org/wx.DC.html#wx.DC.GetTextExtent
        # Return type
        #
        # wx.Size
        # https://docs.wxpython.org/wx.Size.html#wx-size
        textDimensions = finalDC.GetTextExtent(message)
        
        textWidth = textDimensions.x
        textHeight = textDimensions.y
        
        center = wx.Point((clientArea.GetWidth() - textWidth) / 2,
                          (clientArea.GetHeight() - textHeight) / 2 )
        
        finalDC.DrawText(message,
                         center)
        
        finalDC.SelectObject(wx.NullBitmap)
        
    def stretchGameView(self):
        
        clientArea = self.gameWindow.GetClientSize()
        stretchedSize = wx.Size()
        
        
        # Check if we proportionally resize the height OR the width
        if ( clientArea.GetWidth() 
             * 
             self.level.getHeight() 
             / 
             self.level.getWidth() 
             < 
             clientArea.GetHeight()):
        
            stretchedSize.Set( # Set width
                               clientArea.GetWidth(),
                
                               # Set calculated proportional height
                               clientArea.GetWidth() 
                               * 
                               self.level.getHeight() 
                               / 
                               self.level.getWidth() )
        
        else:
            stretchedSize.Set( # Set calculated proportional width
                               clientArea.GetHeight() 
                               * 
                               self.level.getWidth() 
                               / 
                               self.level.getHeight(),
                               
                               # Set height
                               clientArea.GetHeight())
        
        # Now create a backBuffer and stretch it to the correct size
        # wx.Image has member functions that allows us to scale the image
        stretchedImage = self.backBuffer.ConvertToImage()
        stretchedImage = stretchedImage.Scale(stretchedSize.GetWidth(),
                                              stretchedSize.GetHeight())
        
        # https://docs.wxpython.org/wx.MemoryDC.html
        finalDC = wx.MemoryDC()
        imageDC = wx.MemoryDC()
        
        finalDC.SelectObject(self.finalBackBuffer)
        imageDC.SelectObject(stretchedImage.ConvertToBitmap())
        
        finalDC.SetBackground(wx.BLACK_BRUSH)
        finalDC.Clear()
        
        center = wx.Point()
        
        center.x = (clientArea.GetWidth() - stretchedImage.GetWidth()) / 2
        center.y = (clientArea.GetHeight() - stretchedImage.GetHeight()) / 2
        
        # Now copy the stretched image onto the final DC
        #
        # https://docs.wxpython.org/wx.MemoryDC.html
        # Look for .Blit(), it is inherited from wx.DC
        #
        # https://docs.wxpython.org/wx.DC.html
        # Copy from this DC to another DC
        #finalDC.Blit( center,
        #              stretchedSize,
        #              imageDC,
        #              wx.Point(0, 0))
        finalDC.Blit( # xdest 
                      center.x,
                      
                      # ydest
                      center.y,
                      
                      # width
                      stretchedSize.GetWidth(),
                      
                      # height
                      stretchedSize.GetHeight(),
                      
                      # source
                      imageDC,
                      
                      # xsrc 
                      0,
                      
                      # ysrc
                      0)
        
        # Draw a black border around
        # Just want an outline. We don't want anything inside.
        finalDC.SetBrush(wx.TRANSPARENT_BRUSH)
        finalDC.DrawRectangle( wx.Point(0,0),
                               clientArea )
        
        # CLEAR IT WHEN DONE!
        imageDC.SelectObject(wx.NullBitmap)
        finalDC.SelectObject(wx.NullBitmap)
        
    def flipBackBuffer(self):
        
        clientArea = self.gameWindow.GetClientSize()
        
        finalDC = wx.MemoryDC()
        
        screenDC = wx.ClientDC(self.gameWindow)
        
        finalDC.SelectObject(self.finalBackBuffer)
        
        
        # .Blit()
        # https://docs.wxpython.org/wx.DC.html#wx.DC.Blit
        #screenDC.Blit( wx.Point(0, 0),
        #               clientArea,
        #               finalDC,
        #               wx.Point(0, 0))
        screenDC.Blit( # xdest 
                      0,
                      
                      # ydest
                      0,
                      
                      # width
                      clientArea.x,
                      
                      # height
                      clientArea.y,
                      
                      # source
                      finalDC,
                      
                      # xsrc 
                      0,
                      
                      # ysrc
                      0)
        
        
        finalDC.SelectObject(wx.NullBitmap)
    
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
        
        filename = ""
        startingLevel = 0
        
        # Get the number of arguments
        argc = len(sys.argv)
        
        ## DEBUG
        ##
        #print("DEBUG - sys.argv: {}".format(sys.argv))
        #print("DEBUG - argc: {}".format(argc))
        
        
        # wxPython is handling the arguments for us,
        # argc is the number of arguments passed to us
        # We pass in 2 things, the file name and the starting
        # level.
        #
        # We say 3 because the first argument is us which would be
        # CrazyApes app.
        if argc == 3:
           filename = str(argv[1])
           startingLevel = int(argv[2])
        
        # Create the main window
        self.frame = CrazyApesFrame( parent = None,
                                     title = "Crazy Apes",
                                     filename = filename,
                                     startingLevel = startingLevel )
        
        # Show the main window
        self.frame.Show()
        
        return True
        
#--------------------------- Auto-Execute (Start) ------------------------------

if __name__ == "__main__":
    
    app = CrazyApesApp()
    app.MainLoop()
    
#--------------------------- Auto-Execute (End) --------------------------------