import pygame as pg
from przedmioty import *
from ustawienia import *
from przeszkody import Przeszkoda


marg = 20 #margines uzywany pozniej przy krawedziach mapy zeby parszywek nie wyszedl caly za okienko
class Mapa:
    """
    Klasa reprezentująca mapę. Po niej Parszywek ma się poruszać, na niej są kanały, do których jest ograniczony.
    Można do niej dodać przedmioty, które ma zbierać, przeszkody, które ma odblokowywać i wściekłe psy, których ma unikać,
    """
    def __init__(self, indeks: int, tekstura: pg.surface, gra) -> None:
        self.indeks: int = indeks
        self.tekstura: pg.surface = tekstura
        self.gra = gra
        self.polaczenia: dict[str, int] = {} #słownik potrzebny do logiki zmian map, kluczami są kierunki a wartościami indeksy map
        self.przedmioty = []
        self.psy = []
        self.przeszkody = []
    
    def dodaj_polaczenie(self, kierunek: str, indeks_mapy_docelowej: int) -> None:
        self.polaczenia[kierunek] = indeks_mapy_docelowej
        
    def dodaj_psa(self, pies) -> None:
        self.psy.append(pies)

    def dodaj_przedmiot( self, przedmiot) -> None:
        self.przedmioty.append(przedmiot)
    
    def dodaj_przeszkode(self, przeszkoda) -> None:
        self.przeszkody.append(przeszkoda)
    
    def sprawdz_krawedzie(self) -> None:
        gracz = self.gra.gracz
        #wymiary obrazka parszywka ustalone w pliku gracz.py: 70x90
        if gracz.x < marg and "lewo" in self.polaczenia:
            self.zmien_mape(self.polaczenia["lewo"], "lewo")
        elif gracz.x > DLUGOSC - marg - 70 and "prawo" in self.polaczenia:
            self.zmien_mape(self.polaczenia["prawo"], "prawo")
        elif gracz.y < marg and "gora" in self.polaczenia:
            self.zmien_mape(self.polaczenia["gora"], "gora")
        elif gracz.y > WYSOKOSC - marg - 90 and "dol" in self.polaczenia:
            self.zmien_mape(self.polaczenia["dol"], "dol")
    
    def zmien_mape(self, nowy_indeks: int, kierunek: str) -> None:

        self.gra.aktualna_mapa = nowy_indeks
        self.gra.tlo = self.gra.mapy[nowy_indeks].tekstura
        
        gracz = self.gra.gracz
        if kierunek == "lewo":
            gracz.x = DLUGOSC - marg - 70
        elif kierunek == "prawo":
            gracz.x = marg
        elif kierunek == "gora":
            gracz.y = WYSOKOSC - marg - 90
        elif kierunek == "dol":
            gracz.y = marg

    def resetuj(self) -> None:
        for przedmiot in self.przedmioty:
            przedmiot.podniesiony = False
        for pies in self.psy:
            pies.resetuj()
        for przeszkoda in self.przeszkody:
            przeszkoda.aktywna = True

        
