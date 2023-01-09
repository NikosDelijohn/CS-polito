#  Implement the sieve of Eratosthenes.

from math import sqrt, floor

def main():

    # Read input from the user.
    n = int(input("Enter a positive integer: "))

    # Start with all numbers from 2 to n.
    primes = set(range(2, n + 1))

    #                                  ___
    # consider each factor from 2 to \/ n
    for i in range(2, floor(sqrt(n)) + 1):
        for j in range(i ** 2, n + 1, i):  # find the  multiples of  'i' (using a step 'i')
            primes.discard(j)

    # Display primes.
    print("There are", len(primes), "primes less than or equal to", n, ":")
    for p in sorted(primes):
        print(" ", p)

if __name__ == "__main__":

    main()
