import pygame as pg
import os

class Przeszkoda:
    def __init__(self, gra, x, y, obrazek, wymagany_przedmiot=None, kontrolowana_przeszkoda=None):
        self.gra = gra
        self.x = x
        self.y = y
        self.nazwa = obrazek
        self.wymagany_przedmiot = wymagany_przedmiot
        self.aktywna = True
        self.kontrolowana_przeszkoda = kontrolowana_przeszkoda

        sciezka_obrazka = os.path.join("spritey", obrazek)
        self.obraz = pg.image.load(sciezka_obrazka).convert_alpha()
        self.obraz = pg.transform.scale(self.obraz, (90, 90))
        self.rect = self.obraz.get_rect(topleft=(x, y))  

    def rysuj(self, ekran):
        if self.aktywna:
            ekran.blit(self.obraz, (self.x, self.y))

    def dezaktywuj(self):
        self.aktywna = False
        if self.kontrolowana_przeszkoda:
            self.kontrolowana_przeszkoda.aktywna = False

    def koliduje(self, gracz):
        if not self.aktywna:
            return False
            
        gracz_rect = pg.Rect(gracz.x, gracz.y, gracz.obraz.get_width(), gracz.obraz.get_height())
        
        if self.rect.colliderect(gracz.rect):
            if self.wymagany_przedmiot and gracz.odblokowywacz == self.wymagany_przedmiot:
                self.dezaktywuj() 
                gracz.odblokowywacz = None  # zużywamy odblokowywacz
                return False  # już nie blokuje
            return True  # kolizja, ale nie ma odblokowywacza
        return False
