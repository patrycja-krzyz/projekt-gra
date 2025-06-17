from silnik import *
import sys
from przedmioty import * 
from gracz import *
from mapy import *
from wsciekly_pies import *
from ekrany_startowe import *

class Gra: 
    def __init__(self, silnik):
        pg.init()
        self.silnik = silnik
        self.ekran = pg.display.set_mode(RES)
        pg.display.set_caption("Parszywek we Wrocławiu")
        self.zegar = pg.time.Clock()
        self.delta_czas = 1
        self.ekran_startowy = ekran_startowy(self)
        self.ekran_jakgrac = ekran_jakgrac(self)
        self.mapa_wro = mapa_wro(self) 
        self.stan_gry = "start"
        self.gracz = gracz(self)
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

        #tu można dodać więcej połączeń, przedmioty i psów

    def rysuj_interfejs(self):
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

    def sprawdz_zdarzenia(self):
        for zdarz in pg.event.get():
            if zdarz.type == pg.QUIT or (zdarz.type == pg.KEYDOWN and zdarz.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif zdarz.type == pg.KEYDOWN:
                if zdarz.key == pg.K_e:
                    for przedmiot in self.przedmioty:
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
        #for przedmiot in self.przedmioty:
        #   przedmiot.rysuj()
        for pies in self.mapy[self.aktualna_mapa].psy:
            pies.rysuj()
        self.gracz.rysuj()
        self.rysuj_interfejs()                 
        pg.display.flip() 

    def aktualizuj(self):
        self.gracz.aktualizuj()
        self.rysuj()
        for pies in self.mapy[self.aktualna_mapa].psy:
            pies.aktualizuj()
        self.mapy[self.aktualna_mapa].sprawdz_krawedzie()
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

    
