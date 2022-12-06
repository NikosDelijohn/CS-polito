#!/usr/bin/python3 

import sys

def main():

    ok = True
    sum = 0
    even_number = 0
    total_acquisitions = 0
    minimum = sys.maxsize # any number "large enough" should be ok. However, this is the absolute maximum reachable
    maximum = 0

    while ok:
        line = input("Write a number: ")
        if line == "":
            ok = False
        else:
            if not line.isdigit():
                print("This should be a number!")
            else:
                num = int(line)
                if num < minimum:
                    minimum = num
                if maximum < num:
                    maximum = num
                if num % 2 == 0:
                    even_number += 1
                total_acquisitions += 1
                sum = sum + num # OR sum += num
                print(f"Sum: {sum}. Minimum: {minimum}. Maximum: {maximum}. Even numbers: {even_number}. Odd numbers: {total_acquisitions - even_number}")


if __name__ == "__main__":
    main()