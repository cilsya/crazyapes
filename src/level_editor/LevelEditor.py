# wxPython documentation
# https://wxpython.org/Phoenix/docs/html/wx.1moduleindex.html

import wx

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
        
        #------------------
        # Member Variables
        # (End)
        #------------------
        
        #----------------------------------------
        # Create MenuBar
        # (Start)
        #----------------------------------------
        
        self.menuBar = wx.MenuBar()
        
        self.menuFile.Append( Enum_Menu_IDS.ID_New_Package,
                                 "New &Package")
        self.menuFile.Append( Enum_Menu_IDS.ID_New_Level,
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
        self.arrowLeftBitmap = wx.Bitmap(asset_editor_data.ArrowLeft)
        
        # Arrow Right
        self.arrowRightBitmap = wx.Bitmap(asset_editor_data.ArrowRight)
        
        # Execute
        self.executeImage = wx.Bitmap(asset_editor_data.Execute).\
            ConvertToImage()
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
        
        
        self.toolbar.AddTool( Enum_Toolbar_IDS.TLB_PREVIOUS_LEVEL,
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
        
    #----------------------- EVENT CALLBACKS (START) ---------------------------
        
    def OnNewPackage(self, event):
        pass
    
    def OnNewLevel(self, event):
        pass
    
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
        pass
    
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