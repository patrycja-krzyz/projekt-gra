import pygame as pg
from ustawienia import *

import pygame as pg

class Silnik:
    def __init__(self):
        self.wczytaj_teksty()
        self.wczytaj_ui()

    def wczytaj_teksty(self):
        self.mapki = [
            pg.transform.scale(pg.image.load("tekstury/staremiasto.png").convert(), (1280, 720)),
            pg.transform.scale(pg.image.load("tekstury/dworzec.png").convert(), (1280, 720)),
            pg.transform.scale(pg.image.load("tekstury/jakgrac.png").convert(), (1280, 720)),
            pg.transform.scale(pg.image.load("tekstury/krzyki.png").convert(), (1280, 720)),
            pg.transform.scale(pg.image.load("tekstury/mapa.png").convert(), (1280, 720)),
            pg.transform.scale(pg.image.load("tekstury/Nadodrze.png").convert(), (1280, 720)),
            pg.transform.scale(pg.image.load("tekstury/placgrunwaldzki.png").convert(), (1280, 720)),
            pg.transform.scale(pg.image.load("tekstury/pustystarter.png").convert(), (1280, 720)),
            pg.transform.scale(pg.image.load("tekstury/starter.png").convert(), (1280, 720)),
            pg.transform.scale(pg.image.load("tekstury/zoo.png").convert(), (1280, 720)),
            pg.transform.scale(pg.image.load("tekstury/niepolda.png").convert(), (1280, 720))
        ]
        
        #self.mapki = [
        #      pg.transform.scale(pg.image.load("zasoby/tekstury/staremiasto.png").convert(), RES),
        #      pg.transform.scale(pg.image.load("zasoby/tekstury/dworzec.png").convert(), RES),
        #      pg.transform.scale(pg.image.load("zasoby/tekstury/jakgrac.png").convert(), RES),
        #      pg.transform.scale(pg.image.load("zasoby/tekstury/krzyki.png").convert(), RES),
        #      pg.transform.scale(pg.image.load("zasoby/tekstury/mapa.png").convert(), RES),
        #      pg.transform.scale(pg.image.load("zasoby/tekstury/Nadodrze.png").convert(), RES),
        #      pg.transform.scale(pg.image.load("zasoby/tekstury/placgrunwaldzki.png").convert(), RES),
        #      pg.transform.scale(pg.image.load("zasoby/tekstury/pustystarter.png").convert(), RES),
        #      pg.transform.scale(pg.image.load("zasoby/tekstury/starter.png").convert(), RES),
        #      pg.transform.scale(pg.image.load("zasoby/tekstury/zoo.png").convert(), RES),
        #     pg.transform.scale(pg.image.load("zasoby/tekstury/niepolda.png").convert(), RES)
        # ]
        
    def wczytaj_ui(self):
        self.ui_obraz = pg.image.load("spritey/energia.png").convert_alpha()
        self.ui_obraz = pg.transform.scale(self.ui_obraz, (300, 150))
