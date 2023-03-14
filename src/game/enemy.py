# Native modules
from random import randint
import math
import sprite_data

# Custom Modules
import level_data
import sprite

class Enemy(sprite.Sprite):
    
    def __init__(self,
                 lvl,
                 de,
                 s_index,
                 x = 1,
                 y = 1,
                 i_lives = 1):
        
        # Call the constructor of the parent class
        super(Enemy, self).__init__(lvl,
                                    de,
                                    s_index,
                                    x,
                                    y,
                                    i_lives)
        
        self.goal = None
        self.classID = sprite_data.Enum.ENEMY_CLASSID
        
    def addGoal(self,
                g):
        self.goal = g
    
    def move(self,
            x,
            y):
        
       xpos = self.pos.x + x
       ypos = self.pos.y + y
        
       if self.isValidLevelMove(xpos, ypos):
           
           # Make sure enemy (NPC, non-playable character) do not overlap
           # each other.
           for spr in level_data.NPC:
               if spr != self:
                   if spr.getX() == xpos:
                       if spr.getY() == ypos:
                           return False
           
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
    
    
    def idleUpdate(self):
        
        if self.goal is not None:
            self.simulateAI()
            
    def simulateAI(self):
        
        goal_pos = self.goal.getPosition()
        direction = sprite_data.Vector()
        
        direction.x = goal_pos.x - self.pos.x
        direction.y = goal_pos.y - self.pos.y
        
        # Determine x direction
        if direction.x > 0:
            direction.x = 1
        elif direction.x < 0:
            direction.x = -1
        else:
            direction.x = 0
            
        # Determine y direction
        if direction.y > 0:
            direction.y = 1
        elif direction.y < 0:
            direction.y = -1
        else:
            direction.y = 0
        
        # self.move() returns true or false.
        #
        # If it succeeds in moving (true), we exit the method because it never
        # enters the if block.
        #
        # If it does not succeed (false), we could use path finding technics
        # BUT we will just use trial and error, basically a brute force 
        # method. Just going to test to go left, right, or up, and down
        if self.move(direction.x, direction.y) == False:
            
            # While he cannot move in the direction.
            # Create a random value between -1 and 1 in x and y
            is_valid = False
            while is_valid == False:
                is_valid = self.move( randint(-1,1), randint(-1,1))
