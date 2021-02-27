#The Dobble Algorithm - www.101computing.net/the-dobble-algorithm/
from random import shuffle
from dobble import dobble, output_dobble
from st import st_dev, mean
import os
import random
import pygame

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TURKUS = (66, 140, 120)
EMPTY = (0,0,0,0)

WIDTH = 640
HEIGHT = 480
drawingArea = pygame.Rect(0, 0, WIDTH, HEIGHT)

pygame.font.init()
myfont = pygame.font.SysFont('Cambria', 30)
pos = (-1,-1)


# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([WIDTH*2, HEIGHT])

# This sets the name of the window
pygame.display.set_caption('Dobble trainer')

clock = pygame.time.Clock()


# Set positions of graphics
background_position = [0, 0]

# Load and set up graphics.

player_image = pygame.image.load("PNG/apple.png")
player_image = pygame.transform.scale(player_image, (110, 110))
#player_image.set_colorkey(BLACK)




done = 0

cardSurf1 = pygame.surface.Surface((WIDTH, HEIGHT),pygame.SRCALPHA)
cardSurf2 = pygame.surface.Surface((WIDTH, HEIGHT),pygame.SRCALPHA)
lineSurf = pygame.surface.Surface((4, HEIGHT),pygame.SRCALPHA)



#%%
def sur_occ(rect, surface = None, app = False):
    if surface == None:
        surface = []
        
    for r in surface:
        if r.colliderect(rect):
            return False
        
    if app:    
        surface.append(rect)
    return True
#%%

class Symbol:
    
    def __init__(self, nazwa = "empty", czytajObraz = False):
        self.pole = pygame.Rect(0,0,0,0)
        self.name = nazwa
        self.picture = None
        if czytajObraz:
            self.wczytaj_obraz()
            self.update_location()
        
    def wczytaj_obraz(self,dirr = "PNG/", skala = 0.2):
        self.picture = pygame.image.load(dirr+self.name)
        self.picture = pygame.transform.rotozoom(self.picture, random.randrange(360), skala)
        pass
    def update_location(self):
        if self.picture != None:
            self.pole.w = self.picture.get_width()
            self.pole.h = self.picture.get_height()
            
    def skaluj_obraz(self, skala = 1.2):
        self.picture = pygame.transform.smoothscale(self.picture, [int(self.pole.w/skala), int(self.pole.h/skala)])
        self.update_location()
        #print("skaluje")
            
        

class Karta:
    
    def __init__(self, slad_karty, sciezki):
        self.symbols = []
        self.pole = pygame.Rect(0,0,WIDTH,HEIGHT)
        
        for i in range(len(slad_karty)):
            tmp = Symbol(sciezki[slad_karty[i]], czytajObraz=True)
            self.symbols.append(tmp)
        pass
    
    def new_rect_colliding(self, new_rect):  
        for rec in self.symbols:
            if rec.pole.colliderect(new_rect) and not rec.pole is new_rect:
                return True
            
        return False
    
    def rozmiesc(self, ):
        for symbol in self.symbols:
            self.ilosc_prob = 0
            while True:
                self.ilosc_prob += 1
                #print(self.ilosc_prob)
                if (self.ilosc_prob % 200 == 50):
                    symbol.skaluj_obraz()
                        
                symbol.pole.x = random.randrange(self.pole.w - symbol.pole.w)
                symbol.pole.y = random.randrange(self.pole.h - symbol.pole.h)
                if not self.new_rect_colliding(symbol.pole):
                    break
            



    def zmiana_pola(self, w,h, x = 0, y = 0):
        self.pole.update(x, y, w, h)
    
    
    
    

class Talia:
    #from dobble import dobble
    cards = []
    slady_kart = dobble(8)
    sciezki = os.listdir("PNG")
    def __init__(self, ile_kart = len(slady_kart)):
        for i in range(ile_kart):
            tmp = Karta(self.slady_kart[i], self.sciezki)
            self.cards.append(tmp)

            pass

karty = Talia()       
shuffle(karty.cards)


#%%

prost = pygame.Rect(0, 0, 22, 100)
prost.size = (12,34)
prost.size = (66,180)
prost.topleft =(10,111)

prost.center
prost.bottomright
prost.topleft
prost.x
prost.y
prost.w
prost.h


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


#%%

# for sym in katy.cards[1]:
#     pass
#     picture = pygame.image.load("PNG/"+sym.name)
#  #   picture = pygame.transform.rotate(picture, random.randrange(360))
#     picture = pygame.transform.rotozoom(picture, random.randrange(360), .2)
#     sym.w = picture.get_width()
#     sym.h = picture.get_height()
    
# #    picture = pygame.transform.smoothscale(picture, [w,h])
#     ilosc_prob = 0
#     while True:
#         ilosc_prob += 1
#         print(ilosc_prob)
#         x = random.randrange(WIDTH)
#         y = random.randrange(HEIGHT)
#         rect = pygame.Rect(x, y, w, h)
#         if sur_occ(rect,sur,app=True) and drawingArea.contains(rect):
#             break
#     picture = pygame.transform.rotate(picture, random.randrange(33))
# karta1 = karty.cards[random.randrange(57)]
# karta2 = karty.cards[random.randrange(57)]



def blit_karta(karta, cardSurf):
    
    karta.rozmiesc()
    cardSurf.fill(EMPTY)
    for symb in karta.symbols:
        cardSurf.blit(symb.picture, symb.pole.topleft)
    return karta
        
        
        
i = 48

karta1 = blit_karta(karty.cards[i], cardSurf1)
karta2 = blit_karta(karty.cards[i+1], cardSurf2)

czas = Measure()

stats = []

while done == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = -1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos() 
    
    

    
    
    
    T = " "
    for symb in karta1.symbols:
       if symb.pole.collidepoint(pos):
           T += symb.name
           if symb.name in [i.name for i in karta2.symbols]:
               T+= "<"
               i+= 1
               stats.append(czas.get_lap_seconds())
               print("Karta > {} Time: {:.3f}".format(i, stats[-1]))
               pos = (-1, -1)
               try:
                   karta1 = blit_karta(karty.cards[i], cardSurf1)
                   karta2 = blit_karta(karty.cards[i+1], cardSurf2)
               except:
                   done = 1
                   
                   
    if done == 1:
        pass #operacje takie jak przedstawienie wyników
        print("FINALNY CZAS: {:}:{:0>2d}:{:0>3d}".format(*czas.get_total()))
        
        srednia = mean(stats)
        odchylenie = st_dev(stats)
        print("Średnia: {:.2f} odchylenie standardowe: {:.2f}".format(srednia,odchylenie))

        with open("wyniki.txt", "a") as file:
            file.write("{:.0f}\t{:.3f}\t{:.3f}\t\n".format(czas.get_total_seconds(),srednia,odchylenie))
        
        
    if done == -1:
        pass #operacje takie jak przedstawienie wyników
        print("GRA ZAKOŃCZONA PRZED KOŃCEM: {:}:{:0>2d}:{:0>3d}".format(*czas.get_total()))         
               
               
            


    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    # player_position = pygame.mouse.get_pos()
    # x = player_position[0]
    # y = player_position[1]
    
    # Copy image to screen:
    # screen.blit(player_image, [x, y])
    
    # Copy image to screen:
    #screen.blit(background_image, background_position)
    screen.fill(TURKUS)
    lineSurf.fill(BLACK)
    
    screen.blit(cardSurf1,(0,0))
    screen.blit(cardSurf2,(WIDTH,0))
    screen.blit(lineSurf,(WIDTH - lineSurf.get_width()//2, 0))
    
    textsurface = myfont.render(str(pos) + T, False, (0, 0, 0))    
    screen.blit(textsurface,(0,0))
    
    pygame.display.flip()

    clock.tick(60)
    

pygame.quit ()

