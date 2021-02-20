#The Dobble Algorithm - www.101computing.net/the-dobble-algorithm/
from random import shuffle
from dobble import dobble, output_dobble
import os
import random





"""
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/4YqIKncMJNs
 Explanation video: http://youtu.be/ONAK8VZIcI4
 Explanation video: http://youtu.be/_6c4o41BIms
"""

import pygame

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TURKUS = (66, 140, 120)

WIDTH = 800
HEIGHT = 640
drawingArea = pygame.Rect(0, 0, WIDTH, HEIGHT)

pygame.font.init()
myfont = pygame.font.SysFont('Cambria', 30)
pos = (-1,-1)


# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# This sets the name of the window
pygame.display.set_caption('Dobble trainer')

clock = pygame.time.Clock()


# Set positions of graphics
background_position = [0, 0]

# Load and set up graphics.

player_image = pygame.image.load("PNG/apple.png")
player_image = pygame.transform.scale(player_image, (110, 110))
#player_image.set_colorkey(BLACK)




done = False

game_surf = pygame.surface.Surface((WIDTH, HEIGHT),pygame.SRCALPHA)

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
        
    def wczytaj_obraz(self,dirr = "PNG/", skala = 0.3):
        self.picture = pygame.image.load(dirr+self.name)
        self.picture = pygame.transform.rotozoom(self.picture, random.randrange(360), skala)
        pass
    def update_location(self):
        if self.picture != None:
            self.pole.w = self.picture.get_width()
            self.pole.h = self.picture.get_height()
            
    def skaluj_obraz(self, skala = 2):
        self.picture = pygame.transform.smoothscale(self.picture, [self.pole.w//skala, self.pole.h//skala])
        self.update_location()
        print("skaluje")
            
        

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
                print(self.ilosc_prob)
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
#%%


karty.cards[1].rozmiesc()


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

for symb in karty.cards[0].symbols:
    game_surf.blit(symb.picture, symb.pole.topleft)
    
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos() 
    
    T = " "
    for symb in karty.cards[0].symbols:
       if symb.pole.collidepoint(pos):
           T += symb.name
            


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
    
    screen.blit(game_surf,(0,0))
    
    textsurface = myfont.render(str(pos) + T, False, (0, 0, 0))    
    screen.blit(textsurface,(0,0))
    
    pygame.display.flip()

    clock.tick(60)
    

pygame.quit ()

