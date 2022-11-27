# Esercizio 03.2.3
# Seasonal cycles

# Read input from the user.
month = int(input("Enter the month as an integer: "))
day = int(input("Enter the day as an integer: "))

# Determine the season.
if 1 <= month <= 3:  # oppure: month >= 1 and month <= 3
    season = "Winter"
elif 4 <= month <= 6:
    season = "Spring"
elif 7 <= month <= 9:
    season = "Summer"
elif 10 <= month <= 12:
    season = "Fall"

if month % 3 == 0 and day >= 21:
    if season == "Winter":
        season = "Spring"
    elif season == "Spring":
        season = "Summer"
    elif season == "Summer":
        season = "Fall"
    else:
        season = "Winter"

# Display the result.
print("That day is in", season)
