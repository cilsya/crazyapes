#---------------
# Imports 
# (Start)
#---------------

# Native modules
from random import randint

# Custom modules
import character
import drawEngine

#---------------
# Imports 
# (End)
#---------------

class Enum(object):
    #------------------
    # Static Member variables
    # (Start)
    #------------------
    
    TILE_EMPTY = 0
    TILE_WALL = 1
    
    #------------------
    # Static Member variables
    # (End)
    #------------------

class Level(object):
    
    def __init__(self,
                 de,
                 width = 30,
                 height = 20):
        
        
        self.width = width
        self.height = height
        self.level = [None] * self.width
        self.player = None
        self.drawArea = de
        
        # Making nested list
        for x in range(self.width):
            self.level[x] = [None] * self.height
            
        # Create the level
        self.createLevel()
        
        # Set map
        self.drawArea.setMap(self.level)
        
    def __del__(self):
        
        # Python has garbage collection, do not need to delete
        
        #for x in range(self.width):
        #    self.level[x] = None
        
        #self.level = [None] * self.width
        
        pass
        
    def createLevel(self):
        
        for x in range(self.width):
            for y in range(self.height):
                
                # Random integer between 0 (inclusive) and 99 (inclusive)
                random = randint(0,99)
                
                # Dealing with borders
                if ( y == 0 
                     or 
                     y == self.height - 1 
                     or
                     x == 0
                     or
                     x == self.width - 1):
                    
                    self.level[x][y] = Enum.TILE_WALL
                    
                # Not a border so not necessarily a wall. Randomize it with
                # more bias being and empty space.
                else:
                    
                    # Create an empty
                    # In this case, a 90% chance there will be an empty space
                    #
                    # So a 10% chance of being a wall.
                    #
                    # NOTE: The character will always start on the top left
                    #       corner (1, 1) (if base 1)
                    #       The code (x < 3 and y < 3) is to prevent being 
                    #       fenced in.
                    #      
                    if ( random < 90
                         or
                         (x < 3 and y < 3)):
                             
                        self.level[x][y] = Enum.TILE_EMPTY
                    else:
                        self.level[x][y] = Enum.TILE_WALL
                        
        
    def addPlayer(self,
                  p):
        self.player = p
    
    def update(self):
        # Here is where we deal with fireballs moving and extra things
        pass
    
    def draw(self):
        self.drawArea.drawBackground()
    
    def keyPress(self,
                 c):
        
        if self.player is not None:
            if self.player.keyPress(c) == True:
                return True
                
        return False
        
        # We need to draw the level
        pass