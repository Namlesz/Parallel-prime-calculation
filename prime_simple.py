import math
import sys
import time


def isPrime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True

    for i in range(2, math.ceil(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


def main():
    print("Program wyznaczający liczby pierwsze z zakresu [1,N]")
    n = 0
    primesCount = 0
    if len(sys.argv) <= 1:
        n = int(input("Podaj N: "))
    else:
        n = int(sys.argv[1])

    start_time = time.time()  # start timer for prime calculations

    for i in range(0, n):
        if isPrime(i):
            primesCount += 1
            if len(sys.argv) > 2 and sys.argv[2] == "print":
                print(i)

    end_time = time.time() - start_time  # end timer for prime calculations

    print("Wyznaczono " + str(primesCount) + " liczb pierwszych.")
    print("Czas wyznaczania liczb pierwszych: " + str(end_time) + " sekund.")
    print("Kończe działanie programu.")


main()
