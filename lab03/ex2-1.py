# Exercise 03.2.1
# Trends

def main():
    # Read three numbers from the user.
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    # Determine and display their status.
    if num1 < num2 and num2 < num3:
        print("They are in increasing order.")
    elif num1 > num2 and num2 > num3:
        print("They are in decreasing order.")
    else:
        print("They are neither in increasing order nor decreasing order.")

    # Note that you could also write
    # if num1 < num2 < num3:
    # sine python applies "comparison chaining"
    # see: https://docs.python.org/3/reference/expressions.html#comparisons

if __name__ == "__main__":
    main()