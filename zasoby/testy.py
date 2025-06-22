import unittest
from gracz import *
from przedmioty import *
from przeszkody import *
from mapy import *
from unittest.mock import Mock

class Test(unittest.TestCase):
    def test_resetuj(self):
        mock_gra= Mock()
        g = gracz(mock_gra) ## tworzę ,,podróbkę" obiektu
        g.x, g.y, g.energia = 999, 888, 12 ## jakaś zmiana
        g.resetuj() ## uruchomienie funkcji
        self.assertEqual(g.x, 700) 
        self.assertEqual(g.y, 400)
        self.assertEqual(g.energia, 100) ##ręczne ustawienie
    
    def test_czy_przegrana(self):
        mock_gra = Mock()
        mock_gra.stan_gry = "gra" ## ustawiamy poczatkowy stan gry
        g = gracz(mock_gra)
        g.energia = 0
        g.czy_przegrana()
        self.assertEqual(g.gra.stan_gry, "gameover")

    def test_podnies(self):
        mock_gracz = Mock()
        mock_gracz.odblokowywacz = None
        mock_gracz.przedmioty_zebrane = [] ##nic nie trzyma
        mock_gracz.energia = 50
        mock_gra = Mock()
        mock_gra.gracz = mock_gracz
        p = Przedmiot(mock_gra, 0, 0, "ser.png")
        p.nazwa = "ser"
        p.podnies()
        self.assertIn(p.obraz, mock_gracz.przedmioty_zebrane) ##sprawdzenie, czy jest na liscie
        self.assertEqual(mock_gracz.energia, 80)

    def test_koliduje(self):
        mock_gra = Mock()
        przeszkoda = Przeszkoda(mock_gra, 0, 0, "autobus.png", wymagany_przedmiot="bilet")
        przeszkoda.rect = Mock()
        przeszkoda.rect.colliderect = lambda rect: True ##udajemy ze jest kolizja
        gracz_mock = Mock()
        gracz_mock.x = 0
        gracz_mock.y = 0
        gracz_mock.rect = Mock()
        gracz_mock.odblokowywacz = "bilet"

        self.assertFalse(przeszkoda.koliduje(gracz_mock))

    def test_zmien_mape(self):
        mock_gra = Mock()
        mock_gra.mapy = [Mock(), Mock()]
        mock_gra.gracz = Mock()
        mapa = Mapa(0, Mock(), mock_gra)
        mapa.zmien_mape(1, "prawo")
        self.assertEqual(mock_gra.aktualna_mapa, 1)



if __name__ == '__main__':
    unittest.main()