# Exercise 03.2.2
# Grades

def main():
    # Read the letter grade from the user.
    letter = input("Enter a letter grade: ")

    # convert to uppercase to facilitate computation
    letter = letter.upper()

    # Convert the letter portion of the grade to a number.
    if letter[0] == "A":
        num = 4.0
    elif letter[0] == "B":
        num = 3.0
    elif letter[0] == "C":
        num = 2.0
    elif letter[0] == "D":
        num = 1.0
    else:
        num = 0.0

    # Handle the + or - if it is present.
    if len(letter) > 1 and letter[0] != "F":
        if letter[1] == "+" and letter[0] != "A":
            num = num + 0.3
        elif letter[1] == "-":
            num = num - 0.3

    # Display the result.
    print(f"The numeric value is {num}.")

if __name__ == "__main__":
    main()