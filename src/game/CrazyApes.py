# wxPython documentation
# https://wxpython.org/Phoenix/docs/html/wx.1moduleindex.html

import wx

class ID_list(object):
    
    #-------------------------
    # Static Member Variables
    # (Start)
    #-------------------------
    
    ID_New = 400
    ID_Load = 401
    ID_About = 402
    ID_Exit = 403
    
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
        
        # Window(parent, id=ID_ANY, pos=DefaultPosition, size=DefaultSize,
        # style=0, name=PanelNameStr)
        self.gameWindow = wx.Window(self.panel, 
                                    wx.ID_ANY,
                                    wx.DefaultPosition,
                                    wx.Size(200, 200),
                                    wx.BORDER_STATIC)
        
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
        
        # Bind call backs to menu objects
        #self.menuFile.Bind(wx.EVT_MENU, self.OnAbout)
        
        # Bind action to menu : menu wxPython Python Tutorial
        #
        # http://www.java2s.com/Tutorial/Python/
        # 0380__wxPython/Bindactiontomenu.htm
        self.Bind(wx.EVT_MENU, self.OnAbout, self.menuFile_about)
        
    def OnNew(self, event):
        pass
    
    def OnLoad(self, event):
        pass
    
    def OnAbout(self, event):
        
        # https://wxpython.org/Phoenix/docs/html/wx.functions.html#wx.MessageBox
        wx.MessageBox("The Crazy Apes game. Can you survive?",
                      "About Crazy Apes")
        
        # DEBUG
        #
        # wxPython not binding callbacks to events properly
        #
        # https://stackoverflow.com/questions/4242147/
        # wxpython-not-binding-callbacks-to-events-properly/4242889#4242889
        print("DEBUG - Menu Item Selected: {}".format(
                self.menuFile.FindItemById(event.Id).Label) )
    
    def OnExit(self, event):
        pass
    
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