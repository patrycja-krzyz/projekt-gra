from silnik import *

class Gra:
    def __init__(self):
        pg.init()
        self.ekran = pg.display.set_mode(RES)
        self.zegar = pg.time.Clock()
        self.delta_czas = 1
    