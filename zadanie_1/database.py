import sqlite3

def create_table(max_repeats, databasefile="flights.db"):
    # podlacz baze danych SQLite
    
    # proponowane podejscie: jesli parametr 0, nic nie rob
    # jesli wiekszy od 0, usun tabele i utworz nowa
    if max_repeats > 0:
        # tutaj kod



    # zamknij polaczenie z baza danych
    


def save_to_db(flight_df, databasefile="flights.db"):
    # napisz kod zapisania do bazy danych SQLite

def load_flight_data(databasefile="flights.db"):
    # napisz kod odczytania danych z bazy danych SQLite
    # return flight_df