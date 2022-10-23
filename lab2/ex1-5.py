#!/usr/bin/python3

# `**` operator is raise to the power of 
EPSILON = 8.854 * (10 ** (-12))
PI      = 3.14

def main():

    Q1 = float(input("Q1 (in Coulomb): "))
    Q2 = float(input("Q2 (in Coulomb): "))
    r  = float(input("r (in meters): "))

    F = (Q1 * Q2) / (4 * PI * EPSILON * (r**2))

    print(f"The electric force is {F} N.")


if __name__ == "__main__":
    main()