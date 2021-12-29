import math


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

    primeNumbersCount = 0
    n = int(input("Podaj N: "))
    for i in range(0, n):
        if isPrime(i):
            primeNumbersCount += 1
            print(i)

    print("Wyznaczono " + str(primeNumbersCount) + " liczb pierwszych.")
    print("Kończe działanie programu")


main()
