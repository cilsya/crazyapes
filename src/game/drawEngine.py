#--------------------------- Import (Start) ------------------------------------

# Native Modules

# Third-Party Modules
import wx

# Custom modules
import utilities
import define_data

#--------------------------- Import (End) --------------------------------------


class DrawEngine(object):
    
    def __init__( self,
                  xSize = 30,
                  ySize = 20):
        
        #-----------------
        # Member variables
        # (Start)
        #-----------------
        
        self.screenWidth = xSize
        self.screenHeight = ySize
        self.spriteImage = [None] * 16
        self.tileImage = [None]*16
        self.map = None
        
        #wx.Bitmap
        # https://wxpython.org/Phoenix/docs/html/wx.Bitmap.html
        self.winCanvas = None
        
        
        #-----------------
        # Member variables
        # (End)
        #-----------------
        
    def __del__(self):
        
        ## DEBUG
        ##
        #print("DEBUG - Destructor called")
        
        # Put cursor at the end
        #self.gotoxy(0, self.screenHeight)
        
        pass
    
    def createSprite( self,
                      index,
                      
                      #wx.Bitmap
                      # https://wxpython.org/Phoenix/docs/html/wx.Bitmap.html
                      sprite):
        """
        NOTE: We might be loading bitmap images. However, you can select 
              white color and mask it out.
        """
        
        # Clamp index within range
        if (index >= 0 and index < 16):
            
            # NOTE: We need to set the mask color. We can do that if we 
            #       convert it to an wxImage first.
            #
            # https://wxpython.org/Phoenix/docs/html/wx.Image.html#wx-image
            img = sprite.ConvertToImage()
            img.SetMaskColour(255, 255, 255)
            
            # Put it in array/list again BUT as a wxBitmap type, not wxImage
            # type
            self.spriteImage[index] = wx.Bitmap(img)
            return index
        
        # If we got this far, it is an error
        return -1
    
    def deleteSprite(self,
                     index,
                     posx,
                     posy):
        
        # In this implementation, we don't need it
        
        # go to the correct location
        # draw the image
        pass
    
    def eraseSprite(self,
                    posx,
                    posy):
        
        # When calling wx.MemoryDC()
        # PyNoAppError: The wx.App object must be created first!
        #wx_App = wx.App()
        
        # https://wxpython.org/Phoenix/docs/html/wx.MemoryDC.html
        dc = wx.MemoryDC()
        
        # This allows us to take a bitmap and associate it with a dc.
        dc.SelectObject(self.winCanvas)
        
        # Draw the actual bitmap
        dc.DrawBitmap( # Assuming the element 0 is the background image
                       self.tileImage[0],
            
                       # https://wxpython.org/Phoenix/docs/html/wx.Point.html
                       wx.Point(posx * define_data.GRID_SIZE,
                                posy * define_data.GRID_SIZE),
                       
                       # Want to use the mask
                       True)
        
        # NOTE: MUST DISASSOCIATE THE BITMAP WITH THE DEVICE CONTEXT AFTER
        #       DONE USING IT.
        dc.SelectObject(wx.NullBitmap)
    
    def drawSprite(self,
                   index,
                   posx,
                   posy):
        
        # When calling wx.MemoryDC()
        # PyNoAppError: The wx.App object must be created first!
        #wx_App = wx.App()
        
        # https://wxpython.org/Phoenix/docs/html/wx.MemoryDC.html
        dc = wx.MemoryDC()
        
        # This allows us to take a bitmap and associate it with a dc.
        dc.SelectObject(self.winCanvas)
        
        # Draw the actual bitmap
        dc.DrawBitmap( self.spriteImage[index],
            
                       # https://wxpython.org/Phoenix/docs/html/wx.Point.html
                       wx.Point(posx * define_data.GRID_SIZE,
                                posy * define_data.GRID_SIZE),
                       
                       # Want to use the mask
                       True)
        
        # NOTE: MUST DISASSOCIATE THE BITMAP WITH THE DEVICE CONTEXT AFTER
        #       DONE USING IT.
        dc.SelectObject(wx.NullBitmap)
        

    def setMap(self,
               data):
        self.map = data

    def createBackgroundTile(
            self,
            index,
            
            #wx.Bitmap
            # https://wxpython.org/Phoenix/docs/html/wx.Bitmap.html
            tile):
    
        if ( index >= 0
             and
             index < 16):
            
            # NOTE: We need to set the mask color. We can do that if we 
            #       convert it to an wxImage first.
            #
            # https://wxpython.org/Phoenix/docs/html/wx.Image.html#wx-image
            img = tile.ConvertToImage()
            img.SetMaskColour(255, 255, 255)
            
            # Put it in array/list again BUT as a wxBitmap type, not wxImage
            # type
            self.tileImage[index] = wx.Bitmap(img)

    def drawBackground(self):
        
        # https://wxpython.org/Phoenix/docs/html/wx.MemoryDC.html
        dc = wx.MemoryDC()
        
        # This allows us to take a bitmap and associate it with a dc.
        dc.SelectObject(self.winCanvas)
        
        # Make sure map is set, meaning not None
        if self.map is not None:
            
            # Looping row by row, but our data is set column by column
            # So do a loop down the y coordinates then by the x coordinates
            for y in range(self.screenHeight):
                
                for x in range(self.screenWidth):
                    
                    # Draw the actual bitmap
                    dc.DrawBitmap( 
                        # Assuming the element 0 is the background image
                        self.tileImage[ self.map[x][y] ],
                        
                        # https://wxpython.org/Phoenix/docs/html/wx.Point.html
                        wx.Point(x * define_data.GRID_SIZE,
                                 y * define_data.GRID_SIZE),
                                   
                        # Want to use the mask
                        True )
        
        # NOTE: MUST DISASSOCIATE THE BITMAP WITH THE DEVICE CONTEXT AFTER
        #       DONE USING IT.
        dc.SelectObject(wx.NullBitmap)
        
    def setWindow(
            self,
            
            #wx.Bitmap
            # https://wxpython.org/Phoenix/docs/html/wx.Bitmap.html
            in_bitmap,
            
            width = 30,
            height = 20 ):
        """
        Set member variables
        """
        
        self.winCanvas = in_bitmap
        self.screenWidth = width
        self.screenHeight = height
