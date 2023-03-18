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
        
        self.gameWindow = None
        self.toolbar = None
        self.menuFile = wx.Menu()
        
        # For the game editor
        self.package = []
        self.levelIndex = None
        self.currentLevel = None
        
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
        
        #-----------------------------------------
        # Bind Callbacks
        # (Start)
        #-----------------------------------------
        
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