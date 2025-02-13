from Importfunctions import *

class Timefunctions:
    def __init__(self, duration, methods = None, repeat = None, autostart = False):
        self.duration = duration
        self.repeat = repeat
        self.startingtime = 0
        self.timeractive = False
        self.methods = methods
        if autostart: self.starttimefunc()
    
    def starttimefunc(self):
        self.timeractive = True
        self.startingtime = pygame.time.get_ticks()

    def endtimefunc(self):
        self.timeractive = False
        self.startingtime = 0
        if self.repeat: self.starttimefunc()
        
    def __bool__(self):
        return self.timeractive


    def update(self):
        if pygame.time.get_ticks() - self.startingtime >= self.duration:
            if self.methods and self.startingtime != 0:
                self.methods()
            self.endtimefunc()