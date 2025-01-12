from unittest.mock import patch
import sqlite3
import tempfile
import os
from zadanie_1.flight_data import fetch_flight_data
from zadanie_1.database import load_flight_data

@patch('zadanie_1.flight_data.requests.get')
def test_fetch_flight_data(mock_get):
    # Przykładowa odpowiedź API
    mock_response = {
        "states": [
            ["abc123", "CALL123", "USA", None, None, -85.0, 32.0, None, True, 250.0, 180.0, 0.0, None, 10000.0, None, None, 0]
        ]
    }
    mock_get.return_value.json.return_value = mock_response

    # Tworzymy tymczasowy plik bazy danych
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as temp_db:
        databasefile = temp_db.name

    try:
        # Wywołujemy fetch_flight_data z poprawnym argumentem databasefile
        fetch_flight_data(databasefile)

        # Sprawdzamy, czy dane zostały zapisane do bazy
        flight_df = load_flight_data(databasefile)
        assert not flight_df.empty, "Dane nie zostały zapisane do bazy"
        assert "icao24" in flight_df.columns, "Brakuje kolumny 'icao24' w zapisanych danych"
        assert flight_df.iloc[0]['icao24'] == "abc123", "Niewłaściwe dane w kolumnie 'icao24'"

    finally:
        # Usuwamy plik tymczasowy po zakończeniu testu
        os.remove(databasefile)
