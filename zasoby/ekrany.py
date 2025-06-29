import pygame as pg 
from ustawienia import *

class Ekran_startowy():
    """
    Ta i następne klasy "ekranowe" reprezentują, to co się będzie wyświetlać w okienku, gdy stan_gry nie równa się "gra".
    To jest ekran od którego się wszystko zaczyna i tu ląduje gracz, jak chce zagrać ponownie - po wygranej lub przegranej.
    """
    def __init__(self, gra) -> None:
        self.gra = gra 
        self.tlo = pg.transform.scale(pg.image.load("tekstury/starter.png").convert(), RES)
        self.przycisk_startu = pg.image.load("spritey/rozpocznijgre_sprite.png").convert_alpha()
        #self.tlo = pg.transform.scale(pg.image.load("zasoby/tekstury/starter.png").convert(), RES)
        #self.przycisk_startu = pg.image.load("zasoby/spritey/rozpocznijgre_sprite.png").convert_alpha()
        self.przycisk_startu = pg.transform.scale(self.przycisk_startu, (150, 130))
        self.start_rect = self.przycisk_startu.get_rect(topleft=(400, 580))
        self.przycisk_jakgrac = pg.image.load("spritey/jakgrac_sprite.png").convert_alpha()
        #self.przycisk_jakgrac = pg.image.load("zasoby/spritey/jakgrac_sprite.png").convert_alpha()
        self.przycisk_jakgrac = pg.transform.scale(self.przycisk_jakgrac, (150, 130))
        self.jakgrac_rect = self.przycisk_jakgrac.get_rect(topleft=(660, 580))
        self.parszywek1 = pg.image.load("spritey/parszywek11.png").convert_alpha()   
        self.parszywek2 = pg.image.load("spritey/parszywek2.png").convert_alpha()      
        self.parszywek3 = pg.image.load("spritey/parszywek3.png").convert_alpha()
        self.parszywki = [        #z tej listy korzysta metoda rysuj, żeby obrazki przedstawiające Parszywka się zmieniały (zwykły, mrugający i machający ogonem)
            pg.transform.scale(self.parszywek1, (90, 90)),
            pg.transform.scale(self.parszywek2, (90, 90)),
            pg.transform.scale(self.parszywek3, (90, 90))
        ]
        self.nr_parszywka = 0
        self.zegar = pg.time.get_ticks()


    def sprawdz_zdarzenia(self) -> None:
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
    
    
    def rysuj(self) -> None:
        self.gra.ekran.blit(self.tlo, (0, 0))
        self.gra.ekran.blit(self.przycisk_startu, self.start_rect)
        self.gra.ekran.blit(self.przycisk_jakgrac, self.jakgrac_rect)
        teraz = pg.time.get_ticks()
        if teraz - self.zegar > 300:
            self.nr_parszywka = (self.nr_parszywka + 1) % 3
            self.zegar = teraz
        self.gra.ekran.blit(self.parszywki[self.nr_parszywka], (760, 280))
        pg.display.flip()


class Ekran_jakgrac:
    """z in strukcjami jak grać"""
    def __init__(self, gra) -> None:
        self.gra = gra 
        self.tlo = pg.transform.scale(pg.image.load("tekstury/jakgrac.png").convert(), RES)
        #self.tlo = pg.transform.scale(pg.image.load("zasoby/tekstury/jakgrac.png").convert(), RES)
        self.start_rect = pg.Rect(930, 640, 160, 150)

    def sprawdz_zdarzenia(self) -> None:
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
    
    def rysuj(self) -> None:
        self.gra.ekran.blit(self.tlo, (0, 0))
        pg.display.flip()


class Mapa_wro():
    def __init__(self, gra) -> None:
        self.gra = gra 
        self.tlo = pg.transform.scale(pg.image.load("tekstury/mapa.png").convert(), RES)
        #self.tlo = pg.transform.scale(pg.image.load("zasoby/tekstury/mapa.png").convert(), RES)

    def sprawdz_zdarzenia(self) -> None:
        for zdarz in pg.event.get():
            if zdarz.type == pg.KEYDOWN:
                if zdarz.key == pg.K_m:
                    self.gra.stan_gry = "gra"
        return None 

    def rysuj(self) -> None:
        self.gra.ekran.blit(self.tlo, (0, 0))
        pg.display.flip()


class Ekran_gameover():
    """To się wyświetla jak graczowi spadnie energia do zera."""
    def __init__(self, gra) -> None:
        self.gra = gra 
        self.tlo = pg.transform.scale(pg.image.load("tekstury/gameover.png").convert(), RES)
        #self.tlo = pg.transform.scale(pg.image.load("zasoby/tekstury/gameover.png").convert(), RES)
        self.start_znowu_rect = pg.Rect(1000, 630, 120, 120)

    def sprawdz_zdarzenia(self)-> None:
        mysz_pos = pg.mouse.get_pos()
        
        for zdarz in pg.event.get(): 
            if zdarz.type == pg.QUIT:
                pg.quit()
                exit()
            if zdarz.type == pg.MOUSEBUTTONDOWN and zdarz.button == 1: 
                if self.start_znowu_rect.collidepoint(mysz_pos):
                    self.gra.resetuj()

        return None
    
    def rysuj(self)-> None:
        self.gra.ekran.blit(self.tlo, (0, 0))
        pg.display.flip()
        

class Ekran_wygrana():
    """
    Pojawia się przy kolizji z Siwkiem, gdy ma się wszystkie prezenty - oznacza wygraną.
    Siwek znajduje się na tym ekranie.
    """
    def __init__(self, gra) -> None:
        self.gra = gra
        self.tlo = pg.transform.scale(pg.image.load("tekstury/welldone.png").convert(), RES)
        self.przycisk_restartu_rect = pg.Rect(1000, 630, 120, 120)  
        self.siwek1 = pg.image.load("spritey/siwek1.png").convert_alpha()   
        self.siwek2 = pg.image.load("spritey/siwek2.png").convert_alpha()      
        self.siwki = [
            pg.transform.scale(self.siwek1, (150, 150)),
            pg.transform.scale(self.siwek2, (170, 170)),
        ]
        self.nr_siwka = 0
        self.zegar = pg.time.get_ticks()

    def sprawdz_zdarzenia(self) -> None:
        mysz_pos = pg.mouse.get_pos()

        for zdarz in pg.event.get():
            if zdarz.type == pg.QUIT:
                pg.quit()
                exit()
            if zdarz.type == pg.MOUSEBUTTONDOWN and zdarz.button == 1:
                if self.przycisk_restartu_rect.collidepoint(mysz_pos):
                    self.gra.resetuj()

        return None

    def rysuj(self) -> None:
        self.gra.ekran.blit(self.tlo, (0, 0))
        teraz = pg.time.get_ticks()
        if teraz - self.zegar > 300:
            self.nr_siwka = (self.nr_siwka + 1) % 2
            self.zegar = teraz
        if self.nr_siwka == 0:
            self.gra.ekran.blit(self.siwki[0], (500, 320))
        elif self.nr_siwka == 1:
            self.gra.ekran.blit(self.siwki[1], (500, 300))
        pg.display.flip()
