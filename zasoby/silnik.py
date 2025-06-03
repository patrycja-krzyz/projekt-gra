import pygame as pg



class silnik:
    def __init__(self,gra):
        self.gra=gra
        self.ekran= gra.ekran

    @staticmethod
    def pobierz_teksture():