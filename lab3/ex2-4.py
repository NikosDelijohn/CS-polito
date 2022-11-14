# Exercise 03.2.4
# Leap years

# Read input from the user.
year = int(input("Enter a year: "))

# Display its status.
if year % 4 != 0 or (year % 100 == 0 and year > 1582 and year % 400 != 0):
    print(year, "is not a leap year.")
else:
    print(year, "is a leap year.")
