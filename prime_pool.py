import math
import time
import multiprocessing as mp
from multiprocessing import Manager

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


# Obsługa procesów
def calculatePrimeList(prime_range, lock, currentNumber, primesCount, toPrint):
    numberToCheck = 0

    while prime_range >= currentNumber.value:  # Działaj dopóki nie przekroczysz zakresu
        lock.acquire()  # Zablokowanie wspólnej pamięci
        numberToCheck = currentNumber.value  # Pobranie wartości do sprawdzenia
        currentNumber.value += 1  # Ustawienie na następną wartość do sprawdzenia
        lock.release()  # Odblokowanie pamięci wspólnej

        if isPrime(numberToCheck):  # Jezeli pierwsza to obsłuz
            if toPrint == "y":
                print(numberToCheck)
            primesCount.value += 1


if __name__ == "__main__":
    pool = mp.Pool(mp.cpu_count())  # Pobranie ilości CPU
    with Manager() as manager:
        print("Program wyznaczający liczby pierwsze z zakresu [1,N]")
        n = int(input("Podaj N: "))
        print_primes = input("Wypisać znalezione liczby pierwsze? (y/n): ")

        lock = manager.Lock()
        start_number = manager.Value(int, 1)
        prime_count = manager.Value(int, 0)

        start_time = time.time()  # Uruchomienie czasomierza

        # Wystartowanie procesów
        pool.apply(
            calculatePrimeList,
            args=(n, lock, start_number, prime_count, print_primes),
        )
        pool.close()
        pool.join()

        end_time = time.time() - start_time  # Zatrzymanie czasomierza

        print("Wyznaczono " + str(prime_count.value) + " liczb pierwszych.")
        print("Czas wyznaczania liczb pierwszych: " + str(end_time) + " sekund.")
        print("Kończe działanie programu.")
