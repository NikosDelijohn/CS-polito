#!/usr/bin/python3

from math import sqrt

def main():

    number = int(input("Write a number here: "))
    for n in range(number + 1):
        divisible = False
        # if we look at the math, we need values between 2 and the square root of the number we're looking for
        for divider in range(2, int(sqrt(n)) + 1):
            if not divisible:
                divisible = (n % divider) == 0
        prime = not divisible
        if n < 2:
            prime = False
        if prime:
            print(n)


if __name__ == "__main__":
    main()