from silnik import *
import sys

class Gra:
    def __init__(self):
        pg.init()
        self.ekran = pg.display.set_mode(RES)
        self.zegar = pg.time.Clock()
        self.delta_czas = 1

    def sprawdz_zdarzenia(self):
        for zdarz in pg.event.get():
            if zdarz.type == pg.QUIT or (zdarz.type == pg.KEYDOWN and zdarz.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
    
    def graj(self):
        while True:
            self.sprawdz_zdarzenia()

if __name__=="__main__":
    gra=Gra()
    gra.graj()
    