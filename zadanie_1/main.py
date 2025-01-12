import schedule
import time
from zadanie_1.database import create_table
from zadanie_1.flight_data import fetch_flight_data, plot_flight_data

def main(interval, max_repeats):
    create_table(max_repeats)
    
    # Licznik iteracji
    counter = 0

    def job_wrapper():
        nonlocal counter
        if counter < max_repeats:
            fetch_flight_data()
            counter += 1
        else:
            print("All tasks completed. Stopping scheduler...")
            return schedule.CancelJob

    # Harmonogram z job_wrapper
    schedule.every(interval).seconds.do(job_wrapper)

    # Pętla główna
    while counter < max_repeats:
        schedule.run_pending()
        time.sleep(1)  # Krótkie opóźnienie zmniejsza obciążenie CPU


if __name__ == '__main__':
    FETCH_INTERVAL = 60  # Czas w sekundach między iteracjami, można inna wartosc
    MAX_REPEATS = 10  # Maksymalna liczba iteracji
    # uwaga: ustawiajac MAX_REPEATS = 0 odcztujemy zapisany plik bazy danych
    main(FETCH_INTERVAL, MAX_REPEATS)
    # Po zakończeniu harmonogramu generuj wykresy
    plot_flight_data()
