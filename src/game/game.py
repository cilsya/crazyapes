#---------------
# Imports 
# (Start)
#---------------


# Native modules

# Python clock say use time.clock for benchmarking.
# NOTE: Implemented differently on each system.
# https://stackoverflow.com/questions/156330/get-timer-ticks-in-python
import time

# This is windows specific
import msvcrt

# Custom modules
import character
import drawEngine
import level
import level_data

#---------------
# Imports 
# (End)
#---------------

class Game(object):

    def __init__(self):

        #--------------------
        # Member Variables
        # (Start)
        #--------------------
        
        # Do not update if less than frame count update
        #
        # NOTE: Time is in seconds NOT milliseconds
        # 
        #       If we want to run at about 30 frames per second, 
        #       1000/30 = 33.333 #THIS IS MILLISECONDS
        #       0.033333
        self.game_speed = 0.033333
        
        self.key = " "
        self.frameCount = 0.0
        self.currentTime = 0.0
        self.startTime = 0.0
        self.lastTime = 0.0
        
        self.drawArea = drawEngine.DrawEngine()
        self.player = None
        
        self.level = None
        
        #--------------------
        # Member Variables
        # (End)
        #--------------------

    def run(self):

        # Clear Row of any writing in the console like the folder path
        #self.drawArea.clear_row(row=1)
        #self.drawArea.clear_row_range(row_range=[0, 5])
        self.drawArea.clear_screen()
        self.drawArea.gotoxy(0,0)
        
        level_width = 30
        level_height = 20
        self.level = level.Level(self.drawArea,
                                 width = level_width,
                                 height = level_height)
        
        self.drawArea.createBackgroundTile(level_data.Enum.TILE_EMPTY,
                                           " ")
        self.drawArea.createBackgroundTile(level_data.Enum.TILE_WALL,
                                          "+")
        
        # ASCII character codes
        #self.drawArea.createBackgroundTile(level_data.Enum.TILE_WALL,
        #                                   chr(219))
        
        self.drawArea.createSprite(level_data.Enum_Entity.SPRITE_PLAYER,
                                   "o")
        self.drawArea.createSprite(level_data.Enum_Entity.SPRITE_ENEMY,
                                   "$")
        self.player = character.Character(self.level, self.drawArea, 0)
        
        # Only need to draw the level once
        self.level.draw()
        self.level.addPlayer(self.player)
        self.level.addEnemies(3)
        
        # Player keyboard button that was pressed
        self.key = " "
        
        # https://stackoverflow.com/questions/85451/
        # pythons-time-clock-vs-time-time-accuracy
        # time.clock() in Python 3 is deprecated
        #
        # Use either time.process_time()
        # https://docs.python.org/3/library/time.html#time.process_time
        #
        # or time.perf_counter()
        # https://docs.python.org/3/library/time.html#time.perf_counter
        #
        # The difference seem to depend on if you want to include sleep or
        # not.
        self.startTime = time.perf_counter()
        self.frameCount = 0
        self.lastTime = 0
        
        self.player.move(0, 0)
        
        #-----------------------------------------------------------------------
        # Main Game Loop
        # (START)
        #-----------------------------------------------------------------------
        
        while self.key != 'q':
            while self.getInput() == False:
                self.timerUpdate()
                
            self.level.keyPress(self.key)

        #-----------------------------------------------------------------------
        # Main Game Loop
        # (END)
        #-----------------------------------------------------------------------

        # Clear everything
        self.drawArea.clear_row_range(row_range=[0, level_height])

        ## Put cursor to draw at the end
        #self.drawArea.gotoxy(0,level_height)

        ## DEBUG
        ##
        #print("DEBUG - Do you see me - A?", flush=False)
        #print("DEBUG - Do you see me - B?", flush=False)
        #print("DEBUG - Do you see me - C?", flush=False)
        #print("DEBUG - Do you see me - D?", flush=False)
        #print("DEBUG - Do you see me - E?", flush=False)
        #print("DEBUG - Do you see me - F?", flush=False)
        
        # Print out information when we quit the game loop
        #
        # Put cursor a few rows down
        #self.drawArea.clear_screen()
        self.drawArea.gotoxy(0,7)
        
        tuple_cursor_position = self.drawArea.get_cursor_position()
        print("Current cursor position: {}".format(tuple_cursor_position))
        fps = self.frameCount / (time.perf_counter() - self.startTime)
        print("{} fps".format(fps))
        print("{} seconds".format(time.perf_counter() - self.startTime))
        print("{} frameCount".format(self.frameCount))
        print("{} time.perf_counter()".format(time.perf_counter()))
        print("{} self.lastTime".format(self.lastTime))
        self.currentTime = time.perf_counter() - self.lastTime
        print("{} self.currentTime".format(self.currentTime))
        print("End of game")
            
        return True
    
    def getInput(self):
        
        # TODO: Find equivalent in Python
        if msvcrt.kbhit():
            
            try:
                # msvcrt.getch() returns a byte literal.
                # Must decode to utf-8
                # https://stackoverflow.com/questions/41918836/
                # how-do-i-get-rid-of-the-b-prefix-in-a-string-in-python/
                # 41918864
                self.key = msvcrt.getch().decode('utf-8')
                return True
            except:
                return False
            
        return False
    
    def timerUpdate(self):
        self.currentTime = time.perf_counter() - self.lastTime
        
        if self.currentTime < self.game_speed:
            return
        
        # Update the level
        self.level.update()
        
        self.frameCount += 1
        self.lastTime = time.perf_counter()
