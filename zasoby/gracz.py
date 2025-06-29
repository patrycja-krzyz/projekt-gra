import pygame as pg
from ustawienia import *
import os

class Gracz():
    """Reprezentuje gracza-Parszywka"""
    def __init__(self, gra) -> None:
        self.gra = gra
        self.x, self.y = 700, 400
        self.szybkosc = 5
        self.energia = 100
        self.odblokowywacz = None
        self.przedmioty_zebrane = []
        self.zebrane_nazwy = []

        self.obraz = pg.image.load("spritey/parszywek1.png").convert_alpha()
        self.obraz = pg.transform.scale(self.obraz, (70, 90))
        self.rect = self.obraz.get_rect(topleft=(self.x, self.y))

        self.dozwolony_kolor = (219, 187, 104)
        self.poprzednie_x = self.x
        self.poprzednie_y = self.y


    def czy_moze_isc(self, x: float, y:float) -> bool:
        """
        Parszywek jest ograniczony do tunelów za pomocą ograniczenia go do jednego koloru (koloru tunelów).
        Ta metoda sprawdza, czy to ten kolor.
        """
        try:
            kolor = self.gra.ekran.get_at((int(x), int(y)))[:3] 
            return kolor == self.dozwolony_kolor
        except:
            return False

    def ruch(self) -> None:
        klawisze = pg.key.get_pressed()
        dx, dy = 0, 0
        self.poprzednie_x = self.x
        self.poprzednie_y = self.y
        
        if klawisze[pg.K_UP]:  
            dy = -self.szybkosc
        elif klawisze[pg.K_DOWN]:  
            dy = self.szybkosc
        elif klawisze[pg.K_LEFT]:  
            dx = -self.szybkosc
        elif klawisze[pg.K_RIGHT]:  
            dx = self.szybkosc

        nowy_x = self.x + dx
        nowy_y = self.y + dy

        self.x = max(0, min(self.x, 1200))  
        self.y = max(0, min(self.y, 800)) 

        srodek_x = nowy_x + self.obraz.get_width() // 2
        dol_y = nowy_y + self.obraz.get_height()

        if self.x != nowy_x or self.y != nowy_y:            #odejmowanie energii przy chodzeniu
            self.energia = max(0, self.energia - 0.025)  
        
        if self.czy_moze_isc(srodek_x, dol_y):              #jak prawda, że nowe (przyszłe) wspł są na kolorze dozwolonym - idzie (zmieniają się wspł gracza)
            self.x, self.y = nowy_x, nowy_y


    def cofnij_ruch(self) -> None:
        self.x = self.poprzednie_x
        self.y = self.poprzednie_y
        self.rect.topleft = (self.x, self.y)

    def aktualizuj(self) -> None:
        self.ruch()
        self.rect.topleft = (self.x, self.y)
        self.czy_przegrana()

    def rysuj(self) -> None:
        self.gra.ekran.blit(self.obraz, (self.x, self.y))

    def czy_przegrana(self) -> None:
        if self.energia == 0:
            self.gra.stan_gry = "gameover"

    def resetuj(self) -> None:
        self.x = 700
        self.y = 400
        self.energia = 100
        self.odblokowywacz = None
        self.obraz = pg.image.load("spritey/parszywek1.png").convert_alpha()
        self.obraz = pg.transform.scale(self.obraz, (70, 90))
        self.przedmioty_zebrane = []