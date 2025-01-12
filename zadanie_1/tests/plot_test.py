from zadanie_1.flight_data import plot_flight_data
from zadanie_1.database import create_table, save_to_db
import tempfile
import os
import pandas as pd

def test_plot_flight_data():
    # Tworzymy tymczasowy plik bazy danych
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as temp_db:
        databasefile = temp_db.name

    try:
        # Tworzymy tabelę i zapisujemy dane testowe
        create_table(1, databasefile=databasefile)
        
        sample_data = {
            'icao24': ['abc123', 'xyz456'],
            'callsign': ['CALL123', 'CALL456'],
            'origin_country': ['USA', 'Canada'],
            'time_position': [None, None],
            'last_contact': [None, None],
            'long': [-85.0, -83.5],
            'lat': [32.0, 33.5],
            'baro_altitude': [1000, 2000],
            'on_ground': [False, False],
            'velocity': [250.0, 300.0],
            'true_track': [180.0, 190.0],
            'vertical_rate': [0.0, 0.0],
            'sensors': [None, None],
            'geo_altitude': [10000.0, 12000.0],
            'squawk': [None, None],
            'spi': [None, None],
            'position_source': [0, 0]
        }
        
        flight_df = pd.DataFrame(sample_data)
        save_to_db(flight_df, databasefile=databasefile)

        # Wywołujemy funkcję plot_flight_data z parametrem show_plot=False
        try:
            plot_flight_data(databasefile=databasefile, show_plot=False)
        except Exception as e:
            pytest.fail(f"Funkcja plot_flight_data rzuciła wyjątek: {e}")
    finally:
        # Usuwamy plik bazy danych po zakończeniu testu
        os.remove(databasefile)
