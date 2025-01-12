import pandas as pd
import matplotlib.pyplot as plt
import requests

# Funkcja do pozyskania danych z OpenSky Network API
def fetch_flight_data(databasefile="flights.db"):
    # wspolrzedne ATL (Atlanta) w stopniach 
    lon_min, lat_min = -85.4277, 32.6407
    lon_max, lat_max = -83.4277, 34.6407

    # napisz kod do pozyskania danych z OpenSky Network API, pamietaj o zalozeniu konta

    
    # Zapisz dane do bazy danych SQLite
    save_to_db(flight_df)
    print("Data saved to database successfully!")


# Odczyt danych i wygenerowanie wykresu z danych lotniczych
def plot_flight_data(databasefile="flights.db", show_plot=True):
    # Wczytaj dane lotnicze z bazy danych
    flight_df = # to bedzie obiekt typu DataFrame

    # caly kod tutaj (filtracja, konwersja jednostek, sortowanie i wybieranie jednego, rysowanie wykresu)


    plt.grid(True)
    plt.tight_layout()
    # Wyświetlanie wykresu tylko, jeśli show_plot=True
    if show_plot:
        plt.show()
