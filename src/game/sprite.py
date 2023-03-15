import drawEngine
import level_data
import sprite_data

class Sprite(object):
    
    def __init__( self,
                  
                  # Level
                  lvl,
                  
                  # DrawEngine
                  de,
                  
                  s_index,
                  x = 1,
                  y = 1,
                  i_lives = 1):
        
        #------------------
        # Member variables
        # (Start)
        #------------------
        
        self.drawArea = de
        
        self.pos = sprite_data.Vector()
        self.pos.x = x
        self.pos.y = y
        
        self.facingDirection = sprite_data.Vector()
        self.facingDirection.x = 1
        self.facingDirection.y = 0
        
        self.spriteIndex = s_index
        self.numLives = i_lives
        
        self.classID = sprite_data.Enum.SPRITE_CLASSID
        
        self.level = lvl
        
        #------------------
        # Member variables
        # (End)
        #------------------
    
    def __del__(self):
        
        ## erase the dying sprite
        #self.erase(self.pos.x,
        #           self.pos.y)
        pass
        
        
    def getPosition(self):
        return self.pos
    
    def getX(self):
        return self.pos.x
    
    def getY(self):
        return self.pos.y
        
    def addLives(self,
                 num = 1):
        self.numLives += num
    
    def getLives(self):
        return self.numLives
    
    def isAlive(self):
        return (self.numLives > 0)
        
    def move(self, x, y):
        
        # This is the position I intend to move.
        # Check if it is valid
        xpos = int(self.pos.x + x)
        ypos = int(self.pos.y + y)
        
        if(self.isValidLevelMove(xpos, ypos)):
        
            # Erase Sprite
            self.erase(self.pos.x,
                       self.pos.y)
            
            self.pos.x += x
            self.pos.y += y
            
            self.facingDirection.x = x;
            self.facingDirection.y = y;
            
            # Draw Sprite
            self.draw(self.pos.x,
                      self.pos.y)
            
            return True
            
        # If we made it this far, we failed to pass validation
        return False

    def draw(self, x, y):
        self.drawArea.drawSprite(self.spriteIndex,
                                 int(x),
                                 int(y))
    
    def erase(self, x,y):
        self.drawArea.eraseSprite(int(x), int(y))
    
    def isValidLevelMove(self, xpos, ypos):
        """
        Check if we are inside level
        Check to make sure where we are moving to is not a wall tile.
        """
        if self.level.level[xpos][ypos] != level_data.Enum.TILE_WALL:
            return True
            
        return False
        
    #def idleUpdate(self):
    #    # This is for the inherited classes
    #    pass
    
    def setPosition(self,
                    x,
                    y):
        
        # Erase sprite
        self.erase(self.pos.x,
                   self.pos.y)
        
        self.facingDirection.x = -100
        self.facingDirection.y = -100
        
        self.pos.x = x
        self.pos.y = y
        
        # draw sprite
        self.draw(self.pos.x, self.pos.y)
        