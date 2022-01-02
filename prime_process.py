import math
import time
import multiprocessing as mp
from multiprocessing import Manager, Process

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


# Obsłuzenie procesów potomych
def calculatePrimeList(
    prime_range, lock, currentNumber, primesCount, toPrint, stop_process
):
    while stop_process.value == False:  #
        lock.acquire()  # Zablokowanie pamięci wspólnej
        if (
            currentNumber.value > prime_range
        ):  # Jezeli zakres jest mniejszy niz liczba, zatrzymaj proces
            stop_process.value = True
            lock.release()  # Zwolnienie pamieci wspólnej
            return

        numberToCheck = currentNumber.value  # Przypisanie liczby do sprawdzenia
        currentNumber.value += 1  # Ustawienie następnej liczby do sprawdzenia
        lock.release()  # Zwolnienie pamieci wspólnej

        if isPrime(numberToCheck):  # Jezeli pierwsza to obsłuz
            if toPrint == "y":
                print(numberToCheck)
            primesCount.value += 1


if __name__ == "__main__":
    with Manager() as manager:
        print("Program wyznaczający liczby pierwsze z zakresu [1,N]")
        print(
            "Sugerowana maksymalna ilość procesów do uruchomienia to "
            + str(mp.cpu_count())
        )
        process_count = int(input("Podaj liczbę procesów do uruchomienia: "))
        n = int(input("Podaj N: "))

        print_primes = input("Wypisać znalezione liczby pierwsze? (y/n): ")

        lock = manager.Lock()
        start_number = manager.Value(int, 1)
        prime_count = manager.Value(int, 0)
        stop_process = manager.Value(bool, False)
        processes = []

        start_time = time.time()  # Uruchomienie czasomierza
        try:
            for i in range(process_count):  # Utworzenie procesów potomnych
                process = Process(
                    target=calculatePrimeList,
                    args=(
                        n,
                        lock,
                        start_number,
                        prime_count,
                        print_primes,
                        stop_process,
                    ),
                )
                processes.append(process)
                process.start()
        except:
            print("Unable to start process")

        for process in processes:  # Oczekiwanie na zakończenie procesów
            process.join()

        end_time = time.time() - start_time  # Zatrzymanie czasomierza

        print("Wyznaczono " + str(prime_count.value) + " liczb pierwszych.")
        print("Czas wyznaczania liczb pierwszych: " + str(end_time) + " sekund.")
        print("Kończe działanie programu.")
