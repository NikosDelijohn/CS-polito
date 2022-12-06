#!/usr/bin/python3

# Tip: Constants always in UPPERCASE
INT_A = 123
INT_B = 456

def main():
    
    int_sum = INT_A + INT_B
    print(f"{'Sum':10} = {int_sum:15}")

    int_difference = INT_A - INT_B 
    print(f"{'Difference':10} = {int_difference:15}")

    int_produdct = INT_A * INT_B 
    print(f"{'Product':10} = {int_produdct:15}")

    int_average_value = (INT_A + INT_B) / 2
    print(f"{'Average':10} = {int_average_value:15}")

    # Function abs() returns the absolute value
    int_distance = abs(INT_A - INT_B)
    print(f"{'Distance':10} = {int_distance:15}")

    maximum_value = max(INT_A, INT_B)
    print(f"{'Max':10} = {maximum_value:15}")

    minimum_value = min(INT_A, INT_B)
    print(f"{'Min':10} = {minimum_value:15}")


if __name__ == "__main__":
    main()