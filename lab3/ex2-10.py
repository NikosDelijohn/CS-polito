# Exercise 03.2.10
# Back to the comet

#  Determine if a person achieves escape velocity.

from math import sqrt

# Define constants.

G = 6.67e-11  # Gravitational constant
M = 2.2e14  # Mass [kg]
D = 9400  # Diameter [m]
R = D / 2  # Radius

def main():

    # Read input from the user.
    kmh = float(input("Enter the jump velocity in km/h: "))

    # Convert to m/s so that we can use the provided formula.
    v = kmh / 3.6

    # Compute the escape velocity in m/s.
    v_escape = sqrt(2 * G * M / R)

    # Determine if the speed is sufficient to escape and display the result.
    if v >= v_escape:
        print("That was enough to jump off Hayley's Comet and never come back down.")
        mass = R * v * v / (2 * G)
        print(f"The comet would need a mass of {mass:g} kg to have enough gravity to")
        print(f"bring you back.  (Hayley's Comet has a mass of {M:g} kg)")
    else:
        print("At that speed, you'll come back down to Hayley's Comet")

if __name__ == "__main__":
    main()
