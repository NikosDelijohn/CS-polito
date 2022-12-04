# Exercise 03.2.5

def main():
    
    # Read input from the user.
    num = float(input("Enter a numeric grade: "))

    # find the letter
    closest_integer = round(num, 0)
    if closest_integer == 4:
        letter = 'A'
    elif closest_integer == 3:
        letter = 'B'
    elif closest_integer == 2:
        letter = 'C'
    elif closest_integer == 1:
        letter = 'D'
    else:
        letter = 'F'

    # Adding "+" and "-". If the grades is greater than the integer value for more than 0.15, then it will be closer to 0.3 than to 0.0
    # so it "deservs" a "+". Similarly for the "-".
    if letter != 'F':
        delta = num - closest_integer
        if delta >= 0.15:
            letter = letter + '+'
        elif delta <= -0.15:
            letter = letter + '-'

    # Display the result.
    print("The letter grade is %s." % letter)



    # Notice that it is possible to enumerate all the possible grades
    # Hoever. this solution is not very readable or easy to maintain
    # even if it works as intended

    # Convert to a letter grade.
    if num >= 3.85:
        letter = "A"
    elif num >= 3.5:
        letter = "A-"
    elif num >= 3.15:
        letter = "B+"
    elif num >= 2.85:
        letter = "B"
    elif num >= 2.5:
        letter = "B-"
    elif num >= 2.15:
        letter = "C+"
    elif num >= 1.85:
        letter = "C"
    elif num >= 1.5:
        letter = "C-"
    elif num >= 1.15:
        letter = "D+"
    elif num >= 0.85:
        letter = "D"
    elif num >= 0.5:
        letter = "D-"
    else:
        letter = "F"

    # Display the result.
    print("The letter grade is %s." % letter)

if __name__ == "__main__":
    main()