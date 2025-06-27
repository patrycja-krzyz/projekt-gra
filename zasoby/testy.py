import unittest
from gracz import *
from przedmioty import *
from przeszkody import *
from mapy import *
from unittest.mock import Mock, patch
import pygame

class Test(unittest.TestCase):
    @classmethod ##inicjacja pygame
    def setUpClass(cls):
        pygame.init()

    @classmethod
    def tearDownClass(cls):
        pygame.quit()
    
    def test_resetuj(self):
        mock_gra= Mock()
        g = Gracz(mock_gra) ## tworzę ,,podróbkę" obiektu
        g.x, g.y, g.energia = 999, 888, 12 ## jakaś zmiana
        g.resetuj() ## uruchomienie funkcji
        self.assertEqual(g.x, 700) 
        self.assertEqual(g.y, 400)
        self.assertEqual(g.energia, 100) ##ręczne ustawienie
    
    def test_czy_przegrana(self):
        mock_gra = Mock()
        mock_gra.stan_gry = "gra"
        g = Gracz(mock_gra)
        g.energia = 0
        g.czy_przegrana()
        self.assertEqual(g.gra.stan_gry, "gameover")

    def test_podnies(self):
        mock_gracz = Mock()
        mock_gracz.odblokowywacz = None
        mock_gracz.przedmioty_zebrane = [] ##nic nie trzyma
        mock_gracz.energia = 50
        mock_gra = Mock()
        mock_gra.Gracz = mock_gracz
        p = Przedmiot(mock_gra, 0, 0, "ser.png")
        p.nazwa = "ser"
        p.podnies()
        self.assertIn(p.obraz, mock_gracz.przedmioty_zebrane) ##sprawdzenie, czy jest na liscie
        self.assertEqual(mock_gracz.energia, 80)
    

    def test_koliduje_blokuje_gdy_brak_przedmiotu(self):
        pg.init()
        ekran = pg.Surface((1200, 800))
        ekran.fill((219, 187, 104))
        mock_gra = Mock()
        mock_gra.ekran = ekran
        mock_gra.stan_gry = "gra"
        gracz = Gracz(mock_gra)
        gracz.x = 100
        gracz.y = 100
        gracz.odblokowywacz = None
        gracz.rect.topleft = (gracz.x, gracz.y)
        przeszkoda = Przeszkoda(mock_gra, 100, 100, "autobus.png", wymagany_przedmiot="bilet")
        przeszkoda.aktywna = True
        gracz.rect = przeszkoda.rect.copy()
        self.assertTrue(przeszkoda.koliduje(gracz))
        self.assertTrue(przeszkoda.aktywna)

    def test_dezaktywuj_brak_przeszkody(self):
        mock_gra = Mock()
        mock_gra.stan_gry = "gra"
        g = Gracz(mock_gra)
        self.assertTrue(g.aktywna)
        g.dezaktywuj()
        self.assertFalse(g.aktywna)
        self.assertIsNone(g.kontrolowana_przeszkoda)

    def test_zmien_mape(self):
        mock_gra = Mock()
        mock_gra.mapy = [Mock(), Mock()]
        mock_gra.Gracz = Mock()
        mapa = Mapa(0, Mock(), mock_gra)
        mapa.zmien_mape(1, "prawo")
        self.assertEqual(mock_gra.aktualna_mapa, 1)



if __name__ == '__main__':
    unittest.main()