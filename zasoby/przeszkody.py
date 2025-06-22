import pygame as pg
import os

class Przeszkoda:
    def __init__(self, gra, x, y, obrazek, wymagany_przedmiot=None):
        self.gra = gra
        self.x = x
        self.y = y
        self.nazwa = obrazek
        self.wymagany_przedmiot = wymagany_przedmiot
        self.aktywna = True

        sciezka_obrazka = os.path.join("spritey", obrazek)
        self.obraz = pg.image.load(sciezka_obrazka).convert_alpha()
        self.obraz = pg.transform.scale(self.obraz, (90, 90))
        self.rect = self.obraz.get_rect(topleft=(x, y))  

    def rysuj(self, ekran):
        if self.aktywna:
            ekran.blit(self.obraz, (self.x, self.y))  

    def koliduje(self, gracz):
        if not self.aktywna:
            return False

        if self.rect.colliderect(gracz.rect):
            if self.wymagany_przedmiot and gracz.odblokowywacz == self.wymagany_przedmiot:
                self.aktywna = False  # odblokowujemy
                gracz.odblokowywacz = None  # zużywamy odblokowywacz
                return False  # już nie blokuje
            return True  # kolizja, ale nie ma odblokowywacza
        return False
