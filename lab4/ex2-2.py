#!/usr/bin/python3 

import math

HALF_LIFE = 6 * 3600 # seconds
A0 = 1000.0
LAMBDA = math.log(2) / HALF_LIFE
TIME_MAX = 25 * 3600 # seconds

def main(): 

    # for each hour
    for seconds in range(0, TIME_MAX, 3600):
        A = A0 * math.exp(-seconds * LAMBDA)
        print(f"Relative quantity remaining after the {int(seconds / 3600)} hour: {A / A0}")


if __name__ == "__main__":

    main()
