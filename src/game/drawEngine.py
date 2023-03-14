import utilities

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
        
        #-----------------
        # Member variables
        # (End)
        #-----------------
        
        # Set cursor visibility to False
        self.cursorVisibility(False)
        
    def __del__(self):
        
        # Set cursor visibility to True 
        self.cursorVisibility(True)
        
        ## DEBUG
        ##
        #print("DEBUG - Destructor called")
    
    def createSprite( self,
                      index,
                      c ):
        
        # Clamp index within range
        if (index >= 0 and index < 16):
            self.spriteImage[index] = c
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
        self.gotoxy(posx, posy)
        print(" ",
              end="",
              flush=True)
    
    def drawSprite(self,
                   index,
                   posx,
                   posy):
        
        # go to the correct location
        self.gotoxy(posx, posy)
        
        # draw the sprite with
        print(self.spriteImage[index],
              end="",
              flush=True)
        
    def gotoxy( self,
                x,
                y):
        utilities.set_console_cursor_position(x, y)

    def cursorVisibility(self,
                        visibility):
        utilities.set_console_cursor_visibility(visibility)
        
    def clear_row(self,
                  row=1):
        utilities.clear_row(row=row)
        
    def clear_row_range(self,
                        row_range=[0, 5]):
        utilities.clear_row_range(row_range=row_range)