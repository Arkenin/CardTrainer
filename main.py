#The Dobble Algorithm - www.101computing.net/the-dobble-algorithm/
from random import shuffle
from st import st_dev, mean
from measure import Measure
from deck import Talia
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

# Create an 640*2/480 sized screen
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


def blit_karta(karta, cardSurf):
    
    karta.rozmiesc()
    cardSurf.fill(EMPTY)
    for symb in karta.symbols:
        cardSurf.blit(symb.picture, symb.pole.topleft)
    return karta
        
        
        
i = 0
karty = Talia()       
shuffle(karty.cards)

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

