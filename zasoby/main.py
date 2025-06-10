from silnik import *
import sys
from gracz import *

class Gra:
    def __init__(self):
        pg.init()
        self.ekran = pg.display.set_mode(RES)
        self.zegar = pg.time.Clock()
        self.delta_czas = 1
        self.gracz = gracz(self)

    def sprawdz_zdarzenia(self):
        for zdarz in pg.event.get():
            if zdarz.type == pg.QUIT or (zdarz.type == pg.KEYDOWN and zdarz.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
        
    
    def rysuj(self):
        self.ekran.fill((0, 0, 0))  
        self.gracz.rysuj()  
        pg.display.flip()  

    def aktualizuj(self):
        self.gracz.aktualizuj()
        self.aktualizuj()
        self.rysuj()
        self.zegar.tick(FPS) 

    def graj(self):
        while True:
            self.sprawdz_zdarzenia()

if __name__=="__main__":
    gra=Gra()
    gra.graj()
    