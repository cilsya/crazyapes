#---------------
# Imports 
# (Start)
#---------------

# Python clock say use time.clock for benchmarking.
# NOTE: Implemented differently on each system.
# https://stackoverflow.com/questions/156330/get-timer-ticks-in-python
import time

# This is windows specific
import msvcrt

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
        
        #--------------------
        # Member Variables
        # (End)
        #--------------------

    def run(self):

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
        
        while self.key != 'q':
            while self.getInput() == False:
                self.timerUpdate()
                
            print("Here's what you pressed: {}".format(self.key))
            
        # Print out information when we quit the game loop
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
            
            # msvcrt.getch() returns a byte literal.
            # Must decode to utf-8
            # https://stackoverflow.com/questions/41918836/
            # how-do-i-get-rid-of-the-b-prefix-in-a-string-in-python/41918864
            self.key = msvcrt.getch().decode('utf-8')
            return True
            
        return False
    
    def timerUpdate(self):
        self.currentTime = time.perf_counter() - self.lastTime
        

        if self.currentTime < self.game_speed:
            return
        
        self.frameCount += 1
        self.lastTime = time.perf_counter()
        