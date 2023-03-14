import drawEngine
import sprite

class Character(sprite.Sprite):
    
    def __init__(self,
                 de, 
                 s_index,
                 x=1,
                 y=1,
                 lives=3,
                 up_key="w",
                 down_key="s",
                 left_key="a",
                 right_key="d"):
    
        super(Character, self).__init__(de,
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
        
        self.classID = sprite.Enum.CHARACTER_CLASSID
        
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