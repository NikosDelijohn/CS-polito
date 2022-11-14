#!/usr/bin/python3 

from math import sqrt

def main():

    number = int(input("Write a number here: "))
    divisible = False
    # if we look at the math, we need values between 2 and the square root of the number we're looking for
    for divider in range(2, int(sqrt(number)) + 1):
        if not divisible:
            divisible = (number % divider) == 0
    prime = not divisible

    if number < 2:
        prime = False

    print(f"{number} is prime: {prime}")


if __name__ == "__main__":
    main()