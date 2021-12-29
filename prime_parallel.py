import math
import sys
from threading import Thread, Lock

# Calculate Prime by divide number and check % == 0
def isPrime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True

    for i in range(2, math.ceil(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


# Thread procces to handle prime calculations
def processPrimes(n):
    global isRunning, primesCheckArray, current_number

    while isRunning:
        # Lock mutex
        mutex.acquire()
        # Get current value to check is Prime
        valueToCheck = current_number
        # Set next value to check if it's Prime
        current_number += 1
        # If next value i out of range stop program
        if current_number > n:
            isRunning = False
        # Unlock mutex
        mutex.release()

        # Check if value is prime and set True if is prime
        if isPrime(valueToCheck):
            primesCheckArray[valueToCheck] = True


def main():
    global primesCheckArray
    primesCount = 0
    n = 0
    t = 0
    
    print("Program wyznaczający liczby pierwsze z zakresu [1,N]")

    # To do
    # check lenght of sys.argv[1]
    # and if it less than 1 check input else get sys.argv
    n = int(input("Podaj N: "))
    primesCheckArray = [False] * n

    t = int(input("Podaj liczbę wątków do uruchomienia: "))
    threads = []

    # Create 't' threads and start
    try:
        for i in range(t):
            thread = Thread(target=processPrimes, args=(n,))
            threads.append(thread)
            thread.start()
    except:
        print("Unable to start thread")
    # Wait for threads to stop
    for thread in threads:
        thread.join()

    # Print primes
    for i in range(n):
        if primesCheckArray[i]:
            primesCount += 1
            print(i)

    print("Wyznaczono " + str(primesCount) + " liczb(y) pierwszych.")
    print("Kończe działanie programu")


# Define global variables
isRunning = True
current_number = 1
primesCheckArray = []
mutex = Lock()

# Main loop
main()
