from silnik import *
import sys
from przedmioty import Przedmiot 
from gracz import *

class Gra:
    def __init__(self):
        pg.init()
        self.ekran = pg.display.set_mode(RES)
        self.zegar = pg.time.Clock()
        self.delta_czas = 1
        self.gracz = gracz(self)
        self.tlo = pg.image.load("tekstury/staremiasto.png").convert()
        self.tlo = pg.transform.scale(self.tlo, RES) 
        self.przedmioty = [
           #Przedmiot(self,300,300, "tort.png")
        ] 

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
        
    def rysuj(self):
        self.ekran.blit(self.tlo, (0, 0)) 
        for przedmiot in self.przedmioty:
            przedmiot.rysuj()
        self.gracz.rysuj()                 
        pg.display.flip() 

    def aktualizuj(self):
        self.gracz.aktualizuj()
        self.rysuj()
        self.zegar.tick(FPS) 

    def graj(self):
        while True:
            self.sprawdz_zdarzenia()
            self.aktualizuj()

if __name__=="__main__":
    gra=Gra()
    gra.graj()
    