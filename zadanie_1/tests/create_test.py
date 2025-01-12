import sqlite3
import pytest
import os
import tempfile
from zadanie_1.database import create_table

def test_create_table():
    # Tworzymy tymczasowy plik na bazę danych
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as temp_db:
        databasefile = temp_db.name

    try:
        # Wywołujemy funkcję, która tworzy tabelę
        create_table(1, databasefile=databasefile)

        # Otwieramy połączenie, by sprawdzić efekty działania funkcji
        connection = sqlite3.connect(databasefile)
        cursor = connection.cursor()

        # Sprawdzamy, czy tabela została utworzona
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='airport_atl'")
        table_exists = cursor.fetchone()
        assert table_exists is not None, "Tabela airport_atl nie została utworzona"

        # Sprawdzamy kolumny tabeli
        cursor.execute("PRAGMA table_info(airport_atl)")
        columns = [col[1] for col in cursor.fetchall()]
        expected_columns = [
            "icao24", "callsign", "origin_country", "time_position", "last_contact",
            "long", "lat", "baro_altitude", "on_ground", "velocity",
            "true_track", "vertical_rate", "sensors", "geo_altitude",
            "squawk", "spi", "position_source"
        ]

        assert columns == expected_columns, f"Kolumny w tabeli nie zgadzają się. Oczekiwano: {expected_columns}, otrzymano: {columns}"

        connection.close()

    finally:
        # Usuwamy plik tymczasowy po zakończeniu testu
        os.remove(databasefile)
