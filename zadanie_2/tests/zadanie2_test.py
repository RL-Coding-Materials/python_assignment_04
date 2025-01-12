import pytest
from zadanie_2.zadanie2 import Pojazd, Samochod, Autobus, FabrykaPojazdow, FabrykaSamochodow, FabrykaAutobusow

# Test 1: Tworzenie obiektu Samochod i sprawdzanie atrybutów
def test_tworzenie_samochodu():
    samochod = Samochod("Toyota", 2022, liczba_drzwi=4)
    assert samochod._model == "Toyota"
    assert samochod._rok == 2022
    assert samochod.liczba_drzwi == 4

# Test 2: Tworzenie obiektu Autobus i sprawdzanie atrybutów
def test_tworzenie_autobusu():
    autobus = Autobus("Solaris", 2021, liczba_miejsc=50)
    assert autobus._model == "Solaris"
    assert autobus._rok == 2021
    assert autobus.liczba_miejsc == 50

# Test 3: Sprawdzanie gettera, settera i deletera predkosci
def test_predkosc():
    samochod = Samochod("Ford", 2023, liczba_drzwi=4)
    samochod.predkosc = 100
    assert samochod.predkosc == 100
    del samochod.predkosc
    assert samochod.predkosc == 0

# Test 4: Ustawienie prędkości na wartość ujemną (oczekiwany wyjątek)
def test_predkosc_wyjatki():
    samochod = Samochod("BMW", 2023, liczba_drzwi=2)
    with pytest.raises(ValueError, match="Prędkość nie może być ujemna!"):
        samochod.predkosc = -10

# Test 5: Tworzenie fabryki samochodów i produkowanie pojazdu
def test_fabryka_samochodow():
    fabryka = FabrykaSamochodow("Fabryka Samochodów")
    samochod = fabryka.stworz_pojazd("Fiat", 2020, liczba_drzwi=5)
    assert isinstance(samochod, Samochod)
    assert samochod._model == "Fiat"
    assert fabryka.ile_wyprodukowano() == 1

# Test 6: Tworzenie fabryki autobusów i produkowanie pojazdu
def test_fabryka_autobusow():
    fabryka = FabrykaAutobusow("Fabryka Autobusów")
    autobus = fabryka.stworz_pojazd("Volvo", 2019, liczba_miejsc=60)
    assert isinstance(autobus, Autobus)
    assert autobus._model == "Volvo"
    assert fabryka.ile_wyprodukowano() == 1

# Test 7: Wyjątek przy próbie stworzenia pojazdu z nieprawidłowym rokiem
def test_fabryka_zly_rok():
    fabryka = FabrykaSamochodow("Fabryka Samochodów")
    with pytest.raises(ValueError, match="Nieprawidłowy rok produkcji!"):
        fabryka.stworz_pojazd("Fiat", 1899, liczba_drzwi=5)

# Test 8: Test metody klasy utworz_fabryke
def test_utworz_fabryke():
    fabryka_samochodow = FabrykaPojazdow.utworz_fabryke("samochod", "Fabryka Samochodów")
    fabryka_autobusow = FabrykaPojazdow.utworz_fabryke("autobus", "Fabryka Autobusów")
    assert isinstance(fabryka_samochodow, FabrykaSamochodow)
    assert fabryka_samochodow.nazwa == "Fabryka Samochodów"
    assert isinstance(fabryka_autobusow, FabrykaAutobusow)
    assert fabryka_autobusow.nazwa == "Fabryka Autobusów"
