import pygame as pg 
from ustawienia import *

class ekran_startowy():
    
    def __init__(self, gra):
        self.gra = gra 
        self.tlo = pg.transform.scale(pg.image.load("tekstury/starter.png").convert(), RES)
        self.przycisk_startu = pg.image.load("spritey/rozpocznijgre_sprite.png").convert_alpha()
        self.przycisk_startu = pg.transform.scale(self.przycisk_startu, (150, 130))
        self.start_rect = self.przycisk_startu.get_rect(topleft=(400, 580))
        self.przycisk_jakgrac = pg.image.load("spritey/jakgrac_sprite.png").convert_alpha()
        self.przycisk_jakgrac = pg.transform.scale(self.przycisk_jakgrac, (150, 130))
        self.jakgrac_rect = self.przycisk_jakgrac.get_rect(topleft=(660, 580))

    def sprawdz_zdarzenia(self):
        mysz_pos = pg.mouse.get_pos()
    
        for zdarz in pg.event.get(): 
            if zdarz.type == pg.QUIT:
                pg.quit()
                exit()
            if zdarz.type == pg.MOUSEBUTTONDOWN and zdarz.button == 1: 
                if self.start_rect.collidepoint(mysz_pos):
                    self.gra.stan_gry = "gra"
                    self.gra.tlo = self.gra.mapy[0].tekstura
                elif self.jakgrac_rect.collidepoint(mysz_pos):
                    self.gra.stan_gry = "jakgrac" 
        return None
    
    
    def rysuj(self):
        self.gra.ekran.blit(self.tlo, (0, 0))
        self.gra.ekran.blit(self.przycisk_startu, self.start_rect)
        self.gra.ekran.blit(self.przycisk_jakgrac, self.jakgrac_rect)
        pg.display.flip()


class ekran_jakgrac:
    
    def __init__(self, gra):
        self.gra = gra 
        self.tlo = pg.transform.scale(pg.image.load("tekstury/jakgrac.png").convert(), RES)
        self.start_rect = pg.Rect(930, 640, 160, 150)

    def sprawdz_zdarzenia(self):
        mysz_pos = pg.mouse.get_pos()
        
        for zdarz in pg.event.get(): 
            if zdarz.type == pg.QUIT:
                pg.quit()
                exit()
            if zdarz.type == pg.MOUSEBUTTONDOWN and zdarz.button == 1: 
                if self.start_rect.collidepoint(mysz_pos):
                    self.gra.stan_gry = "gra"
                    self.gra.tlo = self.gra.mapy[0].tekstura

        return None
    
    def rysuj(self):
        self.gra.ekran.blit(self.tlo, (0, 0))
        pg.display.flip()
