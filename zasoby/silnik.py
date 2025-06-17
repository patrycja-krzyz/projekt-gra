import pygame as pg
from ustawienia import *
from gracz import *

import pygame as pg

class Silnik:
    def __init__(self):
        self.ekran = pg.display.set_mode(RES)
        ##self.wczytaj_teksty()
        self.wczytaj_ui()
        self.gracz = gracz(self)

    def wczytaj_teksty(self):
        self.mapki = [
            pg.transform.scale(pg.image.load("tekstury/staremiasto.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/dworzec.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/jakgrac.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/krzyki.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/mapa.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/Nadodrze.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/placgrunwaldzki.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/pustystarter.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/starter.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/zoo.png").convert(), RES),
            pg.transform.scale(pg.image.load("tekstury/niepolda.png").convert(), RES)
        ]
        
        #self.mapki = [
        #   pg.transform.scale(pg.image.load("zasoby/tekstury/staremiasto.png").convert(), RES),
        #   pg.transform.scale(pg.image.load("zasoby/tekstury/dworzec.png").convert(), RES),
        #   pg.transform.scale(pg.image.load("zasoby/tekstury/jakgrac.png").convert(), RES),
        #   pg.transform.scale(pg.image.load("zasoby/tekstury/krzyki.png").convert(), RES),
        #   pg.transform.scale(pg.image.load("zasoby/tekstury/mapa.png").convert(), RES),
        #   pg.transform.scale(pg.image.load("zasoby/tekstury/Nadodrze.png").convert(), RES),
        #   pg.transform.scale(pg.image.load("zasoby/tekstury/placgrunwaldzki.png").convert(), RES),
        #   pg.transform.scale(pg.image.load("zasoby/tekstury/pustystarter.png").convert(), RES),
        #   pg.transform.scale(pg.image.load("zasoby/tekstury/starter.png").convert(), RES),
        #   pg.transform.scale(pg.image.load("zasoby/tekstury/zoo.png").convert(), RES),
        #   pg.transform.scale(pg.image.load("zasoby/tekstury/niepolda.png").convert(), RES)
        #]
        
    def wczytaj_ui(self):
        self.ui_obraz = pg.image.load("spritey/energia.png").convert_alpha()
        #self.ui_obraz = pg.image.load("zasoby/spritey/energia.png").convert_alpha()
        self.ui_obraz = pg.transform.scale(self.ui_obraz, (300, 150))
    def rysuj_interfejs(self, ekran, gracz):
        ui_x, ui_y = 0, WYSOKOSC - self.ui_obraz.get_height()
        self.ekran.blit(self.ui_obraz, (ui_x, ui_y))
        pasek_x = ui_x + 142
        pasek_y = ui_y + 13
        maks_szerokosc = 137
        wysokosc_paska = 30
        energia = max(0, min(100, self.gracz.energia))
        aktualna_szerokosc = int(maks_szerokosc * energia / 100)
        if energia > 60:
            kolor_paska = (0, 255, 0) #zielony
        elif energia > 30:
            kolor_paska = (255, 165, 0) #pomarańczowy
        else:
            kolor_paska = (255, 0, 0) #czerwony

        pg.draw.rect(self.ekran, (50, 50, 50), (pasek_x, pasek_y, maks_szerokosc, wysokosc_paska))
        pg.draw.rect(self.ekran, kolor_paska, (pasek_x, pasek_y, aktualna_szerokosc, wysokosc_paska))

        start_x = ui_x + 180
        start_y = ui_y + 90
        for i, obraz in enumerate(self.gracz.przedmioty_zebrane):
            miniatura = pg.transform.scale(obraz, (30, 30))
            self.ekran.blit(miniatura, (start_x + i * 35, start_y))

