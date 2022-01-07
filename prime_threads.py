import math
import time
import multiprocessing as mp
from threading import Thread

# Sprawdzanie liczby pierwszej poprzez dzielenie
def isPrime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True

    for i in range(2, math.ceil(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


# Obsługiwanie wątku
def processPrimes(n):
    global isRunning, primesCheckArray, current_number  # Zdefiniowanie zmiennych globalnych

    while isRunning:
        # Nie uzywam instrukcji 'with mutex:' ze względu na obciązenie takiego rozwiazania
        # lock() uzywa sporo zasobow pamieci przez co zwalnia nasz program,
        # w naszym rozwiazaniu jezeli watek obliczy te sama wartosc, nie zmieni to naszego koncowego wyniku
        # a takie rozwiazanie jest zdecydowanie szybsze

        # with mutex: (OPCJONALNE)
        # Jezeli następna wartość jest większa niz zakres, zatrzymaj wątki
        if current_number > n:
            isRunning = False
            return

        # Pobierz aktualną wartość do wyliczenia
        valueToCheck = current_number

        # Ustaw następną wartość do wyliczenia
        current_number += 1
        # END 'with mutex:' (OPCJONALNE)

        # Sprawdzenie czy liczba jest pierwsza, i dodanie do tablicy prawdy
        if isPrime(valueToCheck):
            primesCheckArray[valueToCheck] = True


if __name__ == "__main__":
    # Zdefiniowanie zmiennych globalnych
    global primesCheckArray, isRunning, current_number
    isRunning = True
    current_number = 1
    primesCount = 0
    n = 0
    threads_count = 0

    print(
        "Program wyznaczający liczby pierwsze z zakresu [1,N]\n"
        + "Sugerowana maksymalna ilość wątków do uruchomienia to "
        + str(mp.cpu_count())
    )

    # Podanie danych wejściowych
    threads_count = int(input("Podaj liczbę wątków do uruchomienia: "))
    n = int(input("Podaj N: "))
    print_primes = input("Wypisać znalezione liczby pierwsze? (y/n): ")

    # Inicjalizacja tablicy liczb pierwszych (n+1), bo sprawdzamy N liczb a tablica indeksowana od 0
    primesCheckArray = [False] * (n + 1)

    # Inicjalizacja tablicy wątków
    threads = []

    # Utworzenie wątków
    for i in range(threads_count):
        thread = Thread(target=processPrimes, args=(n,))
        threads.append(thread)

    start_time = time.time()  # Uruchomienie czasomierza

    # Uruchomienie wątków
    try:
        for thread in threads:
            thread.start()
    except:
        print("Unable to start thread")

    # Oczekiwanie na zakończenie wszystkich wątków
    for thread in threads:
        thread.join()

    end_time = time.time() - start_time  # Zatrzymanie czasomierza

    # Zliczenie liczb pierwszych i wyświetlenie wyników
    for i in range(n + 1):
        if primesCheckArray[i]:
            primesCount += 1

            if print_primes == "y":
                print(i)

    # Podsumowanie końcowe
    print("Wyznaczono " + str(primesCount) + " liczb pierwszych.")
    print("Czas wyznaczania liczb pierwszych: " + str(end_time) + " sekund.")
    print("Kończe działanie programu.")
