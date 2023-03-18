# wxPython documentation
# https://wxpython.org/Phoenix/docs/html/wx.1moduleindex.html

import wx

from copy import deepcopy as deepcopy

import asset_data
import define_level_editor_data
import asset_editor_data

class Enum_Menu_IDS:
    ID_New_Package = 400
    ID_New_Level = 401
    ID_Load = 402
    ID_Save = 403
    ID_About = 404
    ID_Exit = 405
    
class Enum_Toolbar_IDS:
    TLB_WALL = 500
    TLB_PLAYER = 501
    TLB_ENEMY = 502                                    
    TLB_ERASE = 503
    TLB_PREVIOUS_LEVEL = 504
    TLB_NEXT_LEVEL = 505
    TLB_TEST_LEVEL = 506
    
class Level_Info:
    def __init__(self):
        self.grid_x = None
        self.grid_y = None
        self.grid = None
    
class LevelEditorFrame(wx.Frame):
    """
    https://wxpython.org/Phoenix/docs/html/wx.Frame.html
    """
    
    def __init__(self,parent, title):
        
        #super(LevelEditorFrame, self).__init__( parent,
        #                                        title = title,
        #                                        pos = (100, 100),
        #                                        size = (650, 500) )
        super(LevelEditorFrame, self).__init__( 
                parent,
                title = title,
                pos = (100, 100),
                size = (470, 515),
                style = wx.DEFAULT_FRAME_STYLE | wx.CLIP_CHILDREN )
        
        #------------------
        # Member Variables
        # (Start)
        #------------------
        
        # Controls
        self.gameWindow = None
        self.toolbar = None
        self.menuFile = wx.Menu()
        
        # For the game editor
        self.package = []
        self.levelIndex = None
        self.currentLevel = None
        
        self.items = []
        
        self.backBuffer = None
        self.finalBackBuffer = None
        
        #------------------
        # Member Variables
        # (End)
        #------------------
        
        #----------------------------------------
        # Create MenuBar
        # (Start)
        #----------------------------------------
        
        self.menuBar = wx.MenuBar()
        
        self.menuFile_NewPackage = self.menuFile.Append(
                                                Enum_Menu_IDS.ID_New_Package,
                                               "New &Package")
        self.menuFile_NewLevel = self.menuFile.Append( 
                                            Enum_Menu_IDS.ID_New_Level,
                                            "&New Level")
        self.menuFile.AppendSeparator()
        self.menuFile.Append( Enum_Menu_IDS.ID_Load,
                                 "New &Load")
        self.menuFile.Append( Enum_Menu_IDS.ID_Save,
                                 "New &Save")
        self.menuFile.AppendSeparator()
        self.menuFile.Append( Enum_Menu_IDS.ID_About,
                                 "New &About")
        self.menuFile.AppendSeparator()
        self.menuFile.Append( Enum_Menu_IDS.ID_Exit,
                                 "New E&xit")
        
        self.menuBar.Append(self.menuFile,
                            "&File")
        
        self.SetMenuBar(self.menuBar)
        
        #----------------------------------------
        # Create MenuBar
        # (End)
        #----------------------------------------
        
        # https://wxpython.org/Phoenix/docs/html/wx.Window.html
        self.gameWindow = wx.Window(self, -1)
        
        # https://wxpython.org/Phoenix/docs/html/
        # wx.Frame.html#wx.Frame.CreateStatusBar
        self.CreateStatusBar(3)
        
        # https://wxpython.org/Phoenix/docs/html/
        # wx.Frame.html#wx.Frame.SetStatusText
        self.SetStatusText("Create a New Package to begin creating levels...")
        
        # https://wxpython.org/Phoenix/docs/html/
        # wx.Frame.html#wx.Frame.CreateToolBar
        self.toolbar = self.CreateToolBar(wx.TB_FLAT)
        
        # Empty
        self.emptyImage = wx.Bitmap(asset_data.EmptyTile).ConvertToImage().Scale(
                        define_level_editor_data.TOOLBAR_SIZE,
                        define_level_editor_data.TOOLBAR_SIZE)
        self.emptyImage.SetMask(False)
        #
        # https://wxpython.org/Phoenix/docs/html/
        # wx.Bitmap.html#wx.Bitmap.ConvertToImage
        self.emptyBitmap = self.emptyImage.ConvertToBitmap()
        
        # Wall
        self.wallImage = wx.Bitmap(asset_data.WallTile).ConvertToImage().Scale(
                        define_level_editor_data.TOOLBAR_SIZE,
                        define_level_editor_data.TOOLBAR_SIZE)
        self.wallImage.SetMask(False)
        #
        # https://wxpython.org/Phoenix/docs/html/
        # wx.Bitmap.html#wx.Bitmap.ConvertToImage
        self.wallBitmap = self.wallImage.ConvertToBitmap()
        
        
        # Player
        self.playerImage = wx.Bitmap(asset_data.PlayerTile).\
                         ConvertToImage().Scale(
                         define_level_editor_data.TOOLBAR_SIZE,
                         define_level_editor_data.TOOLBAR_SIZE)
        self.playerImage.SetMaskColour(255, 255, 255)
        self.playerBitmap = self.playerImage.ConvertToBitmap()
        
        # Enemy
        self.enemyImage = wx.Bitmap(asset_data.EnemyTile).\
                         ConvertToImage().Scale(
                         define_level_editor_data.TOOLBAR_SIZE,
                         define_level_editor_data.TOOLBAR_SIZE)
        self.enemyImage.SetMaskColour(255, 255, 255)
        self.enemyBitmap = self.enemyImage.ConvertToBitmap()
        
        # Eraser
        self.eraserImage = wx.Bitmap(asset_editor_data.Eraser).\
                                ConvertToImage().Scale(
                                    define_level_editor_data.TOOLBAR_SIZE,
                                    define_level_editor_data.TOOLBAR_SIZE)
        self.eraserImage.SetMaskColour(255, 255, 255)
        self.eraserBitmap = self.eraserImage.ConvertToBitmap()
        
        # Arrow Left
        self.arrowLeftImage = wx.Bitmap(asset_editor_data.ArrowLeft).\
                                ConvertToImage().Scale(
                                    define_level_editor_data.TOOLBAR_SIZE,
                                    define_level_editor_data.TOOLBAR_SIZE)
        self.arrowLeftImage.SetMaskColour(255, 255, 255)
        self.arrowLeftBitmap = self.arrowLeftImage.ConvertToBitmap()
        
        # Arrow Right
        self.arrowRightImage = wx.Bitmap(asset_editor_data.ArrowRight).\
                                ConvertToImage().Scale(
                                    define_level_editor_data.TOOLBAR_SIZE,
                                    define_level_editor_data.TOOLBAR_SIZE)
        self.arrowRightImage.SetMaskColour(255, 255, 255)
        self.arrowRightBitmap = self.arrowRightImage.ConvertToBitmap()
        
        # Execute
        self.executeImage = wx.Bitmap(asset_editor_data.Execute).\
            ConvertToImage().Scale(
                                    define_level_editor_data.TOOLBAR_SIZE,
                                    define_level_editor_data.TOOLBAR_SIZE)
        self.executeImage.SetMaskColour(255, 255, 255)
        self.executeBitmap = self.executeImage.ConvertToBitmap()
        
        # https://wxpython.org/Phoenix/docs/html/
        # wx.ToolBar.html#wx.ToolBar.AddRadioTool
        #
        # Walls
        self.toolbar.AddRadioTool( Enum_Toolbar_IDS.TLB_WALL,
                                   "Place walls",
                                   self.wallBitmap,
                                   wx.NullBitmap,
                                   "Place walls")
        #
        # Players
        self.toolbar.AddRadioTool( Enum_Toolbar_IDS.TLB_PLAYER,
                                   "Place player",
                                   self.playerBitmap,
                                   wx.NullBitmap,
                                   "Place player")
        #
        # Enemy
        self.toolbar.AddRadioTool( Enum_Toolbar_IDS.TLB_ENEMY,
                                   "Place enemy",
                                   self.enemyBitmap,
                                   wx.NullBitmap,
                                   "Place enemy")
        #
        # Erase
        self.toolbar.AddRadioTool( Enum_Toolbar_IDS.TLB_ERASE,
                                   "Erase items",
                                   self.eraserBitmap,
                                   wx.NullBitmap,
                                   "Erase items")
        #
        self.toolbar.AddSeparator()
        
        self.button_previous_level = self.toolbar.AddTool(
                               Enum_Toolbar_IDS.TLB_PREVIOUS_LEVEL,
                              "Previous level",
                              self.arrowLeftBitmap,
                              "Previous level" )
        self.toolbar.AddTool( Enum_Toolbar_IDS.TLB_NEXT_LEVEL,
                              "Next level",
                              self.arrowRightBitmap,
                              "Next level" )
        
        self.toolbar.AddSeparator()
        
        self.toolbar.AddTool( Enum_Toolbar_IDS.TLB_TEST_LEVEL,
                              "Test level",
                              self.executeBitmap,
                              "Test level" )
        
        # Disable at the moment since we did not create a package for it yet
        self.toolbar.EnableTool(Enum_Toolbar_IDS.TLB_PREVIOUS_LEVEL,
                                False)
        self.toolbar.EnableTool(Enum_Toolbar_IDS.TLB_NEXT_LEVEL,
                                False)
        
        # Create the toolbar
        # This function should be called after you have added tools.
        self.toolbar.Realize()
        
        # Add to items
        self.items.append(self.emptyBitmap)
        self.items.append(self.wallBitmap)
        self.items.append(self.playerBitmap)
        self.items.append(self.enemyBitmap)
        
        #-----------------------------------------
        # Bind Callbacks
        # (Start)
        #-----------------------------------------
        
        # Bind paint event to game window
        self.gameWindow.Bind(wx.EVT_PAINT,
                             self.OnPaint)
        
        # Bind paint event to game window
        self.gameWindow.Bind(wx.EVT_SIZE,
                             self.OnSize)
        
        # Callback - New Package
        self.Bind( wx.EVT_MENU,
                   self.OnNewPackage,
                   self.menuFile_NewPackage )
        
        # Callback - New Level
        self.Bind( wx.EVT_MENU,
                   self.OnNewLevel,
                   self.menuFile_NewLevel )
        
        # Callback - Previous Button
        self.toolbar.Bind( wx.EVT_TOOL,
                                self.OnToolbarClicked)
        
        #-----------------------------------------
        # Bind Callbacks
        # (End)
        #-----------------------------------------
        
        
    #---------------------- Methods (Start) ------------------------------------
        
    def createNewLevel(self):
        
        # https://wxpython.org/Phoenix/docs/html/wx.functions.html?
        # highlight=getnumberfromuser#wx.GetNumberFromUser
        x = wx.GetNumberFromUser( "Enter the number of columns for the "
                                  "new level.",
                                  "Columns:",
                                  "New Level",
                                  10,
                                  0,
                                  100,
                                  self)
        
        # Error checking
        if x < 1:
            return False
            
        # https://wxpython.org/Phoenix/docs/html/wx.functions.html?
        # highlight=getnumberfromuser#wx.GetNumberFromUser
        y = wx.GetNumberFromUser( "Enter the number of rows for the "
                                  "new level.",
                                  "Rows:",
                                  "New Level",
                                  10,
                                  0,
                                  100,
                                  self)
        
        # Error checking
        if y < 1:
            return False
        
        # Create new information for our level
        currentLevel = Level_Info()
        
        ## DEBUG
        ##
        #print("DEBUG - in createNewLevel, currentLevel: {}".format(
        #                                                currentLevel))
        
        # Add the new level to our package.
        self.package.append(currentLevel)
        
        self.levelIndex = len(self.package)
        
        currentLevel.grid_x = x
        currentLevel.grid_y = y
        #
        # My addition
        currentLevel.grid = []
        
        ## Fill in the grid as a string
        #self.currentLevel.grid = ""
        
        ## Concantenate the string
        #for i in range( self.currentLevel.grid_x ):
        #    self.currentLevel.grid = ( self.currentLevel.grid
        #                               +
        #                               str(self.currentLevel.grid_y) )
        
        # Cycle through x and y
        for i in range(currentLevel.grid_x):
            
            # Create an empty list
            currentLevel.grid.append([])
            
            create_sub_list = True
            
            for j in range(currentLevel.grid_y):
                
                
                if create_sub_list == True:
                    
                    # Create an empty sub list
                    currentLevel.grid[i] = []
                    
                    create_sub_list = False
                
                # Put the value in the new slot
                currentLevel.grid[i].append(0)
        
        self.setCurrentLevel(currentLevel)
        
        # Check to see if we have more than 2 levels
        # Enable the buttons on the GUI
        if self.levelIndex >= 2:
            
            # Enable
            self.toolbar.EnableTool(Enum_Toolbar_IDS.TLB_PREVIOUS_LEVEL,
                                    True)
            
            # There is no next level yet, so set it to false.
            self.toolbar.EnableTool(Enum_Toolbar_IDS.TLB_NEXT_LEVEL,
                                    False)
        
        return True
        
    def setCurrentLevel(self,
                        level):
        
        self.currentLevel = level
        
        # Create new back buffer so it is the size of our level
        self.backBuffer = wx.Bitmap( 
           self.currentLevel.grid_x * (define_level_editor_data.GRID_SIZE +1)+1,
           
           self.currentLevel.grid_y * (define_level_editor_data.GRID_SIZE +1)+1)
        
        new_title = "Level Editor for Crazy Apes - Level {}".format(
                                                             self.levelIndex )
        self.SetTitle(new_title)
        
        status_info = "Level Size: {}x{}".format(self.currentLevel.grid_x,
                                                 self.currentLevel.grid_y)
        
        # Number 1 for the second argument because we split the status info
        # and it is the second one we want to update (base 0)
        self.SetStatusText(status_info, 1)
        
        # Using the same variable
        status_info = "Current Level: {}".format(self.levelIndex)
        #
        # Set the THIRD section of the status info
        self.SetStatusText(status_info, 2)
        
        self.updateView()
        
    def updateView(self):
        
        if self.backBuffer is None:
            return
            
        backBufferDC = wx.MemoryDC()
        backBufferDC.SelectObject(self.backBuffer)
        backBufferDC.SetBackground(wx.BLACK_BRUSH)
        backBufferDC.Clear() 
        
        for x in range(self.currentLevel.grid_x):
            for y in range(self.currentLevel.grid_y):
                
                item = self.currentLevel.grid[x][y]
                
                if item >= 0 and item <= 3:
                    
                    # Draw the background first
                    # https://wxpython.org/Phoenix/docs/html/
                    # wx.DC.html#wx.DC.DrawBitmap
                    backBufferDC.DrawBitmap( 
                        self.items[0],
                        x * (define_level_editor_data.GRID_SIZE + 1) + 1,
                        y * (define_level_editor_data.GRID_SIZE + 1) + 1)
                    
                    # Draw in the exact same location but with the item
                    # https://wxpython.org/Phoenix/docs/html/
                    # wx.DC.html#wx.DC.DrawBitmap
                    backBufferDC.DrawBitmap( 
                        self.items[item],
                        x * (define_level_editor_data.GRID_SIZE + 1) + 1,
                        y * (define_level_editor_data.GRID_SIZE + 1) + 1,
                        
                        # INCLUDE THE MASK IN THIS ONE
                        True)
        
        backBufferDC.SetPen( 
                        # https://wxpython.org/Phoenix/docs/html/wx.Pen.html
                        wx.Pen( 
                            
                            # https://wxpython.org/Phoenix/docs/html/
                            # wx.Colour.html#wx.Colour
                            wx.Colour(128, 128, 128)) )
        
        # Draw Grid
        #
        # Draw vertical lines
        # + 1 because it is zero based
        for x in range(self.currentLevel.grid_x + 1):
            
            backBufferDC.DrawLine( 
                wx.Point( x * (define_level_editor_data.GRID_SIZE + 1),
                               0),
                wx.Point( x * (define_level_editor_data.GRID_SIZE + 1),
                          self.currentLevel.grid_y *(
                              define_level_editor_data.GRID_SIZE + 1)) )
        
        # Horizontal lines
        for y in range(self.currentLevel.grid_y + 1):
            
            backBufferDC.DrawLine( 
                wx.Point( 0,
                          y * (define_level_editor_data.GRID_SIZE + 1)),
                wx.Point( self.currentLevel.grid_x * (
                              define_level_editor_data.GRID_SIZE + 1),
                          y * (define_level_editor_data.GRID_SIZE + 1) ))
        
        backBufferDC.SelectObject(wx.NullBitmap)
        
        self.stretchGameView()
        self.flipBackBuffer()
        
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
    
    def stretchGameView(self):
        
        clientArea = self.gameWindow.GetClientSize()
        stretchedSize = wx.Size()
        
        
        # Check if we proportionally resize the height OR the width
        if ( clientArea.GetWidth() 
             * 
             self.currentLevel.grid_y
             / 
             self.currentLevel.grid_x
             < 
             clientArea.GetHeight()):
        
            stretchedSize.Set( # Set width
                               clientArea.GetWidth(),
                
                               # Set calculated proportional height
                               clientArea.GetWidth() 
                               * 
                               self.currentLevel.grid_y
                               / 
                               self.currentLevel.grid_x )
        
        else:
            stretchedSize.Set( # Set calculated proportional width
                               clientArea.GetHeight() 
                               * 
                               self.currentLevel.grid_x 
                               / 
                               self.currentLevel.grid_y,
                               
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
    
    #---------------------- Methods (End) --------------------------------------
    
    #----------------------- EVENT CALLBACKS (START) ---------------------------
    
    def OnNewPackage(self, event):
        
        old_package = self.package
        old_levelIndex = self.levelIndex
        
        self.package = []
        self.levelIndex = 0
        
        # If failed to create a new level
        if self.createNewLevel() == False:
            self.package = old_package
            self.levelIndex = old_levelIndex
        else:
             self.menuFile.Enable( Enum_Menu_IDS.ID_New_Level,
                                  True )
            
             # Disable at the moment since we did not create a package for 
             # it yet
             self.toolbar.EnableTool(Enum_Toolbar_IDS.TLB_PREVIOUS_LEVEL,
                                     False)
             self.toolbar.EnableTool(Enum_Toolbar_IDS.TLB_NEXT_LEVEL,
                                    False)
            
    def OnNewLevel(self, event):
        self.createNewLevel()
    
    def OnLoad(self, event):
        pass
    
    def OnAbout(self, event):
        pass
    
    def OnExit(self, event):
        pass
    
    def OnToolbarClicked(self, event):
        """
        EVT_TOOL_RANGE Time; 26:00 vid 8
        """
        
        ## DEBUG
        ##
        #print("DEBUG - The OnToolbarClicked button was pressed.")
        #print("DEBUG - self.package: {}".format(self.package))
        
        changed = False
        
        # Check the ID that was passed to the event.
        # Going to do different functionality based on the ID.
        if event.GetId() == Enum_Toolbar_IDS.TLB_PREVIOUS_LEVEL:
            
            ## DEBUG
            ##
            #print("DEBUG - The TLB_PREVIOUS_LEVEL button was pressed.")
            #print("DEBUG - self.package: {}".format(self.package))
            
            if self.levelIndex > 1:
                self.levelIndex -= 1
            
            changed = True
            
        elif event.GetId() == Enum_Toolbar_IDS.TLB_NEXT_LEVEL:
            
            if self.levelIndex < len(self.package):
                self.levelIndex += 1
            
            changed = True
        
        # If there was a change
        if changed == True:
            
            for i in range(len(self.package)):
                
                current_package = self.package[i]
                
                if i == self.levelIndex - 1:
                    self.setCurrentLevel(current_package)
                    
                    # Break because we found what we needed
                    break
                    
            # Disable at the moment since we did not create a package for 
            # it yet
            self.toolbar.EnableTool(Enum_Toolbar_IDS.TLB_PREVIOUS_LEVEL,
                                    self.levelIndex != 1)
            self.toolbar.EnableTool(Enum_Toolbar_IDS.TLB_NEXT_LEVEL,
                                    self.levelIndex != len(self.package) )
        
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
        
        # If the back buffer exists, do this
        if self.backBuffer is not None:
            self.stretchGameView()
            self.flipBackBuffer()
            
    def OnPaint(self, event):
        
        # https://wxpython.org/Phoenix/docs/html/wx.PaintDC.html
        #
        # IMPORTANT:
        # - don't store a wx.PaintDC object. 
        # - If you have an EVT_PAINT() handler, 
        #   you must create a wx.PaintDC object within it even if 
        #   you don't actually use it.
        dc = wx.PaintDC(self.gameWindow)
        
        clientArea = self.gameWindow.GetClientSize()
        
        self.finalBackBuffer = wx.Bitmap(clientArea.GetWidth(),
                                         clientArea.GetHeight())
        
        # If there isn't a back buffer
        if self.backBuffer is None:
            
            # Print out the black border that we want it to begin with
            # 
            # No package created
            # No levels created
            # Draw a simple black border
            screenDC = wx.ClientDC(self.gameWindow)
            screenDC.Clear()
            screenDC.DrawRectangle( 0,
                                    0,
                                    clientArea.GetWidth(),
                                    clientArea.GetHeight())
            
        # There is a back buffer, so do this
        else:
            
            self.stretchGameView()
            self.flipBackBuffer()
        
    #----------------------- EVENT CALLBACKS (END) -----------------------------
        
        
        
        
class LevelEditorPanel(wx.Panel):
    """
    Description: This is the panel that goes into the main apps frame.
    """
    
    def __init__( self,
                  parent ):
        super(CrazyApesPanel, self).__init__(parent)
        
class LevelEditorApp(wx.App):
    """
    Description: This is the main app.
    """
    
    def OnInit(self):
        
        # Create the main window
        self.frame = LevelEditorFrame( parent = None,
                                     title = "Level Editor for Crazy Apes")
        
        # Show the main window
        self.frame.Show()
        
        # https://wxpython.org/Phoenix/docs/html/wx.App.html#wx.App.SetTopWindow
        # Set the "main" top level window, which will be used for the parent 
        # of the on-demand output window as well as for dialogs that do 
        # not have an explicit parent set.
        self.SetTopWindow(self.frame)
        
        return True
        
#--------------------------- Auto-Execute (Start) ------------------------------

if __name__ == "__main__":
    
    app = LevelEditorApp()
    app.MainLoop()
    
#--------------------------- Auto-Execute (End) --------------------------------