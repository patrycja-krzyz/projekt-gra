from silnik import *
import sys
from przedmioty import * 
from gracz import *
from mapy import *
from wsciekly_pies import *
from ekrany import *
from przeszkody import Przeszkoda

class Gra: 
    """Główna klasa obsługująca przebieg gry."""

    def __init__(self, silnik) -> None:
        pg.init()
        self.silnik = silnik
        self.ekran = self.silnik.ekran
        self.silnik.wczytaj_teksty()
        pg.display.set_caption("Parszywek we Wrocławiu")
        self.zegar = pg.time.Clock()
        self.delta_czas = 1
        self.gracz = self.silnik.gracz
        self.ekran_startowy = Ekran_startowy(self)
        self.ekran_jakgrac = Ekran_jakgrac(self)
        self.ekran_gameover = Ekran_gameover(self)
        self.mapa_wro = Mapa_wro(self) 
        self.stan_gry = "start"
        self.ui_obraz = self.silnik.ui_obraz
        self.aktualna_mapa = 0
        self.mapy = self.silnik.mapy
        self.tlo = self.mapy[self.aktualna_mapa].tekstura
        self.ekran_wygrana = Ekran_wygrana(self)


    
    def sprawdz_zdarzenia(self) -> None:
        """Obsłuhuje zamykanie gry, podnoszenie przedmiotów, włączanie mapy i zadawanie obrażeń przez psy."""
        for zdarz in pg.event.get():
            if zdarz.type == pg.QUIT or (zdarz.type == pg.KEYDOWN and zdarz.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif zdarz.type == pg.KEYDOWN:
                if zdarz.key == pg.K_SPACE:
                    for przedmiot in self.mapy[self.aktualna_mapa].przedmioty:
                        if przedmiot.sprawdz_kolizje_z_graczem() and not przedmiot.podniesiony:
                            przedmiot.podnies()
                            print("Przedmiot podniesiony!")
                elif zdarz.key == pg.K_m: 
                   self.stan_gry = "mapa"
            elif zdarz.type == pg.USEREVENT:
                for pies in self.mapy[self.aktualna_mapa].psy:
                    pies.calkowite_obrazenia = 0
                self.gracz.obraz = pg.image.load("spritey/parszywek1.png").convert_alpha()
                self.gracz.obraz = pg.transform.scale(self.gracz.obraz, (70, 90))
        

    
    def rysuj(self) -> None:
        self.ekran.blit(self.tlo, (0, 0)) 
        for przedmiot in self.mapy[self.aktualna_mapa].przedmioty:
            przedmiot.rysuj()
        for pies in self.mapy[self.aktualna_mapa].psy:
            pies.rysuj()
        for przeszkoda in self.mapy[self.aktualna_mapa].przeszkody:
            przeszkoda.rysuj(self.ekran)
        self.gracz.rysuj()
        self.silnik.rysuj_interfejs(self.ekran, self.gracz) ##self.rysuj_interfejs() wczesniej                 
        pg.display.flip() 

    def aktualizuj(self) -> None:
        self.gracz.aktualizuj()
        for pies in self.mapy[self.aktualna_mapa].psy:
            pies.aktualizuj()
        self.mapy[self.aktualna_mapa].sprawdz_krawedzie()
        for przeszkoda in self.mapy[self.aktualna_mapa].przeszkody:
            if przeszkoda.koliduje(self.gracz):
                if self.gracz.odblokowywacz == przeszkoda.wymagany_przedmiot:
                    przeszkoda.aktywna = False
                    self.gracz.odblokowywacz = None
                else:
                    self.gracz.cofnij_ruch()
        self.sprawdz_warunki_zwyciestwa() 
        self.rysuj()
        self.zegar.tick(FPS) 

    def resetuj(self) -> None:
        """Resetuje stan gry do początkowego, korzystając też z metod resetowania gracza i map"""
        self.stan_gry = "start"
        self.aktualna_mapa = 0
        self.tlo = self.mapy[self.aktualna_mapa].tekstura
        self.gracz.resetuj()
        for mapa in self.mapy:
            mapa.resetuj()
        
    def graj(self) -> None:
        while True:
            if self.stan_gry == "start":
                self.ekran_startowy.rysuj()
                self.ekran_startowy.sprawdz_zdarzenia()
            elif self.stan_gry == "jakgrac":
                self.ekran_jakgrac.rysuj()
                self.ekran_jakgrac.sprawdz_zdarzenia()
            elif self.stan_gry == "mapa":
                self.mapa_wro.rysuj()
                self.mapa_wro.sprawdz_zdarzenia() 
            elif self.stan_gry == "gameover":
                self.ekran_gameover.rysuj()
                self.ekran_gameover.sprawdz_zdarzenia() 
            elif self.stan_gry == "gra":
                self.sprawdz_zdarzenia()
                self.aktualizuj()
            elif self.stan_gry == "wygrana":
                self.ekran_wygrana.rysuj()
                self.ekran_wygrana.sprawdz_zdarzenia()

    def sprawdz_warunki_zwyciestwa(self) -> None:
        wymagane: set[str] = {"hulajnoga", "ser", "ksiazka", "puzzle", "tort"}
        zebrane: set[str] = set([przedmiot for przedmiot in self.gracz.zebrane_nazwy])
        cel_x, cel_y = 610, 280  
        tolerancja = 50
        gracz_x, gracz_y = self.gracz.x, self.gracz.y
        odleglosc = ((gracz_x - cel_x)**2 + (gracz_y - cel_y)**2)**0.5

        if (odleglosc <= tolerancja and wymagane == zebrane and self.aktualna_mapa == 9):
            self.stan_gry = "wygrana"
        

if __name__ == "__main__":
    silnik = Silnik()
    gra = Gra(silnik)
    silnik.daj_gre_mapom_i_graczowi(gra)
    gra.graj()

    
