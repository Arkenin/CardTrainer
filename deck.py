#Deck, card and symbol class
from dobble import dobble
import pygame
import random
import os


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
    WIDTH = 640
    HEIGHT = 480
    def __init__(self, slad_karty, sciezki):
        self.symbols = []
        self.pole = pygame.Rect(0,0,self.WIDTH,self.HEIGHT)
        
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