from silnik import *
import sys
from przedmioty import * 
from gracz import *
from mapy import *
from wsciekly_pies import *
from ekrany_startowe import *
from przeszkody import Przeszkoda

class Gra: 
    def __init__(self, silnik):
        pg.init()
        self.silnik = silnik
        self.ekran = self.silnik.ekran
        self.silnik.wczytaj_teksty()
        pg.display.set_caption("Parszywek we Wrocławiu")
        self.zegar = pg.time.Clock()
        self.delta_czas = 1
        self.ekran_startowy = ekran_startowy(self)
        self.ekran_jakgrac = ekran_jakgrac(self)
        self.mapa_wro = mapa_wro(self) 
        self.stan_gry = "start"
        self.gracz = self.silnik.gracz
        self.ui_obraz = self.silnik.ui_obraz
        self.aktualna_mapa = 0
        self.mapy = [Mapa(i, mapa, self) for i, mapa in enumerate(self.silnik.mapki)]



        self.mapy[0].dodaj_polaczenie("gora", 5)
        self.mapy[0].dodaj_polaczenie("dol", 1)
        self.mapy[1].dodaj_polaczenie("dol", 3)
        self.mapy[3].dodaj_polaczenie("gora", 1)
        self.mapy[1].dodaj_polaczenie("gora", 0)
        self.mapy[5].dodaj_polaczenie("dol", 0)
        self.mapy[0].dodaj_polaczenie("prawo", 6)
        self.mapy[6].dodaj_polaczenie("lewo", 0)
        self.mapy[6].dodaj_polaczenie("gora", 9)
        self.mapy[9].dodaj_polaczenie("dol", 6)
        self.mapy[0].dodaj_polaczenie("lewo", 10)
        self.mapy[10].dodaj_polaczenie("prawo", 0)
        sciezka_ruch_niepolda = [
            (375, 420),  
            (950, 420), 
            (375, 420)   
        ]

        pies_niepolda = WscieklyPies(self, 375, 420, sciezka_ruch_niepolda)
        self.mapy[10].dodaj_psa(pies_niepolda)
        
        sciezka_grunwald = [
            (290, 230),  
            (840, 230),  
            (290, 230)   
        ]
        pies_grunwald = WscieklyPies(self, 290, 230, sciezka_grunwald, predkosc=2)
        self.mapy[6].dodaj_psa(pies_grunwald)
        
        sciezka_dworzec = [
            (445, 350),  
            (920, 350),  
            (920, 660),
            (920, 350),
            (445, 350)   
        ]
        pies_dworzec = WscieklyPies(self, 445, 350, sciezka_dworzec, predkosc=1.5)  # Wolniejszy
        self.mapy[1].dodaj_psa(pies_dworzec)

        self.przedmioty = [
        ]

        hulajnoga = Przedmiot(self, 685, 685, "hulajnoga.png")
        self.mapy[10].dodaj_przedmiot(hulajnoga)

        ser = Przedmiot( self, 260, 380, "ser.png")
        self.mapy[1].dodaj_przedmiot(ser)

        ksiazka = Przedmiot(self, 460, 300, "ksiazka.png")
        self.mapy[5].dodaj_przedmiot(ksiazka)

        puzzle = Przedmiot(self, 330, 120, "puzzle.png")
        self.mapy[6].dodaj_przedmiot(puzzle)

        tort = Przedmiot(self, 850, 120, "tort.png")
        self.mapy[6].dodaj_przedmiot(tort)

        autobus = Przeszkoda(self, 635, 585, "autobus.png", wymagany_przedmiot = "bilet")
        self.mapy[5].dodaj_przeszkode(autobus)

        bilet = Przedmiot(self, 370, 440, "bilet.png")
        self.mapy[10].dodaj_przedmiot(bilet)

        paniszczurek = Przeszkoda(self, 900, 600, "paniszczurek.png", wymagany_przedmiot = "roza")
        self.mapy[1].dodaj_przeszkode(paniszczurek)

        roza = Przedmiot(self, 405, 170, "roza.png")
        self.mapy[0].dodaj_przedmiot(roza)

        nauczyciel = Przeszkoda(self, 575, 465, "nauczyciel.png", wymagany_przedmiot = "dokument")
        self.mapy[6].dodaj_przeszkode(nauczyciel)

        dokument = Przedmiot(self, 345, 185, "dokument.png")
        self.mapy[3].dodaj_przedmiot(dokument)


     

        #tu można dodać więcej połączeń, przedmioty i psów

    
    def sprawdz_zdarzenia(self):
        for zdarz in pg.event.get():
            if zdarz.type == pg.QUIT or (zdarz.type == pg.KEYDOWN and zdarz.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif zdarz.type == pg.KEYDOWN:
                if zdarz.key == pg.K_e:
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
        

    
    def rysuj(self):
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

    def aktualizuj(self):
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
        self.rysuj()
        self.zegar.tick(FPS) 

    def graj(self):
        while True:
            if self.stan_gry == "start":
                self.ekran_startowy.rysuj()
                self.ekran_startowy.sprawdz_zdarzenia()
            if self.stan_gry == "jakgrac":
                self.ekran_jakgrac.rysuj()
                self.ekran_jakgrac.sprawdz_zdarzenia()
            if self.stan_gry == "mapa":
                self.mapa_wro.rysuj()
                self.mapa_wro.sprawdz_zdarzenia() 
            if self.stan_gry == "gra":
                self.sprawdz_zdarzenia()
                self.aktualizuj()
 
if __name__ == "__main__":
    silnik = Silnik()
    gra = Gra(silnik)
    gra.graj()

    
