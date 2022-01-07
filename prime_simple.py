import math
import time

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


# Główna pętla
if __name__ == "__main__":
    # Podanie danych wejsciowychs
    print("Program wyznaczający liczby pierwsze z zakresu [1,N]")
    primesCount = 0
    n = int(input("Podaj N: "))
    print_primes = input("Wypisać znalezione liczby pierwsze? (y/n): ")

    # Inicjalizacja tablicy liczb pierwszych (n+1), bo sprawdzamy N liczb a tablica indeksowana od 0
    primesCheckArray = [False] * (n + 1)

    start_time = time.time()  # Uruchomienie czasomierza

    # Sprawdzenie N liczb czy są pierwsze
    for i in range(0, n + 1):
        if isPrime(i):
            primesCheckArray[i] = True

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
