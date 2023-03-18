#---------------
# Imports 
# (Start)
#---------------

# Native modules
from random import randint

# Custom modules
import character
import drawEngine
import enemy
import level_data
import sprite_data

#---------------
# Imports 
# (End)
#---------------

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
        
        # Default starting position
        self.startX = 1
        self.startY = 1
        
        # Making nested list
        for x in range(self.width):
            self.level[x] = [None] * self.height
            
        # Create the level
        self.createLevel()
        
        # Set map
        self.drawArea.setMap(self.level)
        
        # Clear the NPC
        level_data.NPC = []
        
    def __del__(self):
        
        # Python has garbage collection, do not need to delete
        
        #for x in range(self.width):
        #    self.level[x] = None
        
        #self.level = [None] * self.width
        
        pass
    
    @classmethod
    def init2( cls,
               de,
               grid,
               grid_x,
               grid_y):
        
        # Call the constructor for itself here
        result_object = cls(de, grid_x, grid_y)
        
        result_object.level = grid
        width = grid_x
        height = grid_y
        
        # Initial starting position for the player
        result_object.startX = 1
        result_object.startY = 1
        
        # Find where the player was set in the loaded level.
        # We want to set it to black but put that information 
        # of where the player to start into our internal variables.
        for x in range(width):
            for y in range(height):
            
                # The value 2 was set to the starting position of the player
                # BECAUSE
                # Enum_Tile_IDS.TILE_PLAYER  has a value of 2 which is 
                # located in
                if result_object.level[x][y] == \
                    level_data.Enum_Tile_IDS.TILE_PLAYER:
                    
                    # Set the tile to empty
                    result_object.level[x][y] = \
                        level_data.Enum_Tile_IDS.TILE_EMPTY
                    result_object.startX = x
                    result_object.startY = y
                    
                    # Found what we are looking for, break out of the loop
                    break
            
            
        result_object.drawArea.setMap( result_object.level )
        
        # This will return the instantiated an object calling the constructor
        return result_object
        
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
                    
                    self.level[x][y] = level_data.Enum.TILE_WALL
                    
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
                             
                        self.level[x][y] = level_data.Enum.TILE_EMPTY
                    else:
                        self.level[x][y] = level_data.Enum.TILE_WALL
                        
        
    def addPlayer(self,
                  p):
        self.player = p
    
    def update(self,
               in_time):
        # Here is where we deal with fireballs moving and extra things
        
        # We keep sprites that are alive
        sprints_to_keep = []
        
        # spr is a sprite
        for spr in level_data.NPC:
            
            spr.setCurrentTime(in_time)
            
            # Now each sprite is timed on its own when it is time to update
            if spr.updateSprite() == True:
                spr.idleUpdate()
            
            if spr.isAlive() == True:
                sprints_to_keep.append(spr)
        
        # We now populated a list of sprites that are alive.
        # We want to CLEAR the member variable lists of level_data.NPC
        # DO NOT DELETE OR SET TO NONE. You will lose the pointer and it
        # will not make it mutable.
        level_data.NPC.clear()
        #
        # Re-populate with list of sprites that are alive
        for spr in sprints_to_keep:
            level_data.NPC.append(spr)
    
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
    
    def addEnemies(self,
                   num,
                   speed = 5):
        """
        Description: NOTE: num = 0 means load enemies on the map.
                           num > 0 means create enemies on random empty tiles.
        """
    
        i = num
        
        # If there are no enemies,
        # Create the enemies according to where they are in the loaded map.
        if num == 0:
            for x in range(self.width):
                for y in range(self.height):
                    
                    if self.level[x][y] == level_data.Enum_Tile_IDS.TILE_ENEMY:
                        
                        temp = enemy.Enemy(self, 
                                           self.drawArea,
                                           level_data.Enum_Entity.SPRITE_ENEMY,
                                           x,
                                           y)
                        
                        # Set the enemy speed
                        #temp.setSpeed(70)
                        temp.setSpeed(speed)
                        
                        temp.addGoal(self.player)
                        self.addNPC(temp)
            
            return
        
        # Create the enemies randomly
        while i > 0:
            
            # self.width - 2 to prevent being generated in the side walls
            # Add 1 because it is zero based
            # int() will get rid of the values after the decimal
            # Random integer between 0 (inclusive) and 100 (inclusive)
            xpos=int((float(randint(0,100))/100.0) * (self.width - 2) + 1)
            ypos=int((float(randint(0,100))/100.0) * (self.height - 2) + 1)
                
            if self.level[xpos][ypos] != level_data.Enum.TILE_WALL:
                temp = enemy.Enemy(self, 
                                   self.drawArea,
                                   level_data.Enum_Entity.SPRITE_ENEMY,
                                   xpos,
                                   ypos)
                
                # Set the enemy speed
                temp.setSpeed(speed)
                
                temp.addGoal(self.player)
                self.addNPC(temp)
                
                # Reduce or decrement i
                i -= 1
                

    def addNPC(self,
               spr):
        level_data.NPC.append(spr)
        
    def numEnemies(self):
        
        list_enemy_type = []
        for enemy in level_data.NPC:
            if enemy.classID == sprite_data.Enum.ENEMY_CLASSID:
                list_enemy_type.append(enemy)
        
        return len(list_enemy_type)
        
    def setPlayerStart(self):
        self.player.setPosition(self.startX,
                                self.startY)
        
    def getWidth(self):
        return self.width
        
    def getHeight(self):
        return self.height
    