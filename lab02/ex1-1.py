#!/usr/bin/python3

# Tip: Constants always in UPPERCASE
INT_A = 123
INT_B = 456

def main():
    
    int_sum = INT_A + INT_B
    print(f"{INT_A} + {INT_B} = {int_sum}")

    int_difference = INT_A - INT_B 
    print(f"{INT_A} - {INT_B} = {int_difference}")

    int_produdct = INT_A * INT_B 
    print(f"{INT_A} x {INT_B} = {int_produdct}")

    int_average_value = (INT_A + INT_B) / 2
    print(f"({INT_A} + {INT_B})/2 = {int_average_value}")

    # Function abs() returns the absolute value
    int_distance = abs(INT_A - INT_B)
    print(f"|{INT_A} - {INT_B}| = {int_distance}")

    maximum_value = max(INT_A, INT_B)
    print(f"max({INT_A},{INT_B}) = {maximum_value}")

    minimum_value = min(INT_A, INT_B)
    print(f"min({INT_A},{INT_B}) = {minimum_value}")


if __name__ == "__main__":
    main()