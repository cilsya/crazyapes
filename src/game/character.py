import drawEngine
import sprite
import sprite_data

class Character(sprite.Sprite):
    
    def __init__(self,
                 # Level
                 lvl,
                 
                 # Draw Engine
                 de,
                 
                 s_index,
                 x=1,
                 y=1,
                 lives=3,
                 up_key="w",
                 down_key="s",
                 left_key="a",
                 right_key="d"):
        
        # Call the constructor of the parent class
        super(Character, self).__init__(lvl,
                                        de,
                                        s_index,
                                        x,
                                        y,
                                        lives)
        
        #------------------
        # Member variables
        # (Start)
        #------------------
        
        self.upKey = up_key
        self.downKey = down_key
        self.leftKey = left_key
        self.rightKey = right_key
        
        self.classID = sprite_data.Enum.CHARACTER_CLASSID
        
        #------------------
        # Member variables
        # (End)
        #------------------
    
    def keyPress(self,
                 c):
        if c == self.upKey:
            return self.move(0,-1)
            
        elif c == self.downKey:
            return self.move(0, 1)
            
        elif c == self.rightKey:
            return self.move(1, 0)
            
        elif c == self.leftKey:
            return self.move(-1, 0)
            
        return False