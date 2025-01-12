import pytest
from zadanie_4.zadanie4 import Figura, Prostokat, Kwadrat, Kolo, pole, polaPowierzchni
import math

# Test 1: Pole klasy Figura (domyślne)
def test_pole_figura():
    figura = Figura()
    assert pole(figura) == 0  # Domyślne pole klasy Figura

# Test 2: Pole Prostokąta
def test_pole_prostokat():
    prostokat = Prostokat(2, 4)
    assert pole(prostokat) == 8  # 2 * 4

# Test 3: Pole Prostokąta po zmianie wymiarów
def test_pole_prostokat_zmiana():
    prostokat = Prostokat(2, 4)
    assert pole(prostokat, 5, 6) == 30  # Zmiana wymiarów na 5x6

# Test 4: Pole Kwadratu
def test_pole_kwadrat():
    kwadrat = Kwadrat(3)
    assert pole(kwadrat) == 9  # 3 * 3

# Test 5: Pole Kwadratu po zmianie boku
def test_pole_kwadrat_zmiana():
    kwadrat = Kwadrat(3)
    assert pole(kwadrat, 5) == 25  # Zmiana boku na 5

# Test 6: Pole Koła
def test_pole_kolo():
    kolo = Kolo(3)
    assert pytest.approx(pole(kolo), rel=1e-3) == math.pi * 9  # π * r^2 = π * 3^2

# Test 7: Pole Koła po zmianie promienia
def test_pole_kolo_zmiana():
    kolo = Kolo(3)
    assert pytest.approx(pole(kolo, 4.0), rel=1e-3) == math.pi * 16  # Zmiana promienia na 4 (float)

