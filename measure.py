#Measure class for timing
import pygame

class Measure():
    
    def __init__(self):
        self.start_time = pygame.time.get_ticks()
        self.lap_time = pygame.time.get_ticks()
        self.minL = 0
        self.secL = 0
        self.milL = 0
        self.minG = 0
        self.secG = 0
        self.milG = 0
        
    def __str__(self):
        self.get_total()
        return "{}:{}:{}".format(self.minG, self.secG, self.milG)
        
        
    def read_lap(self):
        tmp = pygame.time.get_ticks()
        self.milL += tmp - self.lap_time
        self.lap_time = tmp
        while self.milL > 1000:
            self.secL += 1
            self.milL -= 1000
  
        while self.secL > 60:
            self.minL += 1
            self.secL -= 60
            
        return (self.minL, self.secL, self.milL)

    def get_lap(self):
        tmp = self.read_lap()
        self.minL = 0
        self.secL = 0
        self.milL = 0
            
        return tmp
                
    def get_total(self):
        tmp = pygame.time.get_ticks()
        self.milG += tmp - self.start_time
        self.start_time = tmp
        while self.milG > 1000:
            self.secG += 1
            self.milG -= 1000
  
        while self.secG > 60:
            self.minG += 1
            self.secG -= 60
            
        return (self.minG, self.secG, self.milG)
    
    def get_total_seconds(self):
        self.get_total()
        return 60*self.minG + self.secG
    
    def get_lap_seconds(self):
        tmp = self.read_lap()
        tmp = 60*self.minL + self.secL + self.milL/1000
        self.minL = 0
        self.secL = 0
        self.milL = 0
        return tmp
