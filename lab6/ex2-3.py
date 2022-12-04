# Excercise 06.2.3
# Aerodinamic drag

#   Compute the power needed to overcome the drag force of a vehicle.

# Define constant variables.
PROJECTED_AREA = 2.5  # m^2
DRAG_COEFFICIENT = 0.2
AIR_DENSITY = 1.23  # kg/m^3

WATTS_TO_HP = 1 / 746


def main():
    # Gather input from the user.
    kmh = float(input("Enter the speed in kmh: "))
    v = kmh / 3.6  # speed in m/s

    # Compute the power in Watts and horse power.
    p = power(v)
    hp = p * WATTS_TO_HP

    # Display the result.
    print("The car requires %.2f Watts or %.1f horse power." % (p, hp))


def drag_force(v):
    """
    Compute the drag force at a given velocity
    :param v: the velocity of the vehicle (m/s)
    :return: the drag force (N)
    """
    return 0.5 * AIR_DENSITY * v * v * PROJECTED_AREA * DRAG_COEFFICIENT


def power(v):
    """
    Compute the power needed to overcome the drag force at a given velocity
    :param v: the velocity of the vehicle
    :return: the power in Watt
    """
    return drag_force(v) * v


# Call the main function.
if __name__== "__main__":
    main()

