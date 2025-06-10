import pygame as pg
from ustawienia import *
import os

class gracz():
    def __init__(self, gra):
        self.gra = gra
        self.x, self.y = 600, 400
        self.szybkosc = 5
        sciezka_do_obrazka = os.path.join("zasoby", "spritey", "parszywek1.png")
        
        if not os.path.exists(sciezka_do_obrazka):
            raise FileNotFoundError(f"Nie znaleziono pliku: {sciezka_do_obrazka}")
        
        self.obraz = pg.image.load(sciezka_do_obrazka).convert_alpha()
        # self.obraz = pg.transform.scale(self.obraz, (50, 50)) 

    def ruch(self):
        klawisze = pg.key.get_pressed()

        dx, dy = 0, 0
        
        if klawisze[pg.K_w]:  
            dy = -self.szybkosc
        elif klawisze[pg.K_s]:  
            dy = self.szybkosc
        elif klawisze[pg.K_a]:  
            dx = -self.szybkosc
        elif klawisze[pg.K_d]:  
            dx = self.szybkosc

        self.x += dx
        self.y += dy

        self.x = max(0, min(self.x, 1200))  
        self.y = max(0, min(self.y, 800)) 
    
    def aktualizuj(self):
        self.ruch()