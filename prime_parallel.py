import math
import sys
from threading import Thread, Lock
import time

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

        # If next value i out of range stop program
        if current_number > n:
            isRunning = False
            mutex.release()
            return

        # Get current value to check is Prime
        valueToCheck = current_number

        # Set next value to check if it's Prime
        current_number += 1

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

    # If program is not running with num of therads and N, check the input
    if len(sys.argv) >= 3:
        t = int(sys.argv[1])
        n = int(sys.argv[2])
    else:
        t = int(input("Podaj liczbę wątków do uruchomienia: "))
        n = int(input("Podaj N: "))

    primesCheckArray = [False] * n

    threads = []
    start_time = time.time()  # start timer for prime calculations

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

    end_time = time.time() - start_time  # end timer for prime calculations

    # Count primes and print only when 3 argument is print
    for i in range(n):
        if primesCheckArray[i]:
            primesCount += 1

            if len(sys.argv) > 3 and sys.argv[3] == "print":
                print(i)

    print("Wyznaczono " + str(primesCount) + " liczb pierwszych.")
    print("Czas wyznaczania liczb pierwszych: " + str(end_time) + " sekund.")
    print("Kończe działanie programu.")


# Define global variables
isRunning = True
current_number = 1
primesCheckArray = []
mutex = Lock()

# Main loop
main()
