import drawEngine

class Enum(object):
    #------------------
    # Static Member variables
    # (Start)
    #------------------
    
    SPRITE_CLASSID = 0
    CHARACTER_CLASSID = 1
    
    #------------------
    # Static Member variables
    # (End)
    #------------------

class vector(object):
    
    #------------------
    # Static Member variables
    # (Start)
    #------------------
    
    x = None
    y = None
    
    #------------------
    # Static Member variables
    # (End)
    #------------------

class Sprite(object):
    
    def __init__( self,
                  
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
        
        self.pos = vector()
        self.pos.x = x
        self.pos.y = y
        
        self.facingDirection = vector()
        self.facingDirection.x = 1
        self.facingDirection.y = 0
        
        self.spriteIndex = s_index
        self.numLives = i_lives
        
        self.classID = Enum.SPRITE_CLASSID
        
        #------------------
        # Member variables
        # (End)
        #------------------
    
    def __del__(self):
        
        # erase the dying sprite
        self.erase(self.pos.x,
                   self.pos.y)
    
    def getPosition(self):
        return self.pos
    
    def getX(self):
        self.pos.x
    
    def getY(self):
        self.pos.y
        
    def addLives(self,
                 num = 1):
        self.numLives += num
    
    def getLives(self):
        self.numLives
    
    def isAlive(self):
        return (numLives > 0)
        
    def move(self, x, y):
        
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

    def draw(self, x, y):
        self.drawArea.drawSprite(self.spriteIndex,
                                 int(x),
                                 int(y))
    
    def erase(self, x,y):
        self.drawArea.eraseSprite(int(x), int(y))
        