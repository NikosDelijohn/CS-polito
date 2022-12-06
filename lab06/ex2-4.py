# Excercise 06.2.4
# Electrical wire

#  Compute the resistance of a piece of wire.

from math import pi

# Define constant variables.
COPPER_RESISTIVITY = 1.678e-8  # Ω m
ALUMINUM_RESISTIVITY = 2.82e-8  # Ω m


def main():
    length = float(input("Enter the length of a piece of wire (m): "))
    gauge = float(input("Enter its gauge (AWG): "))

    print("For copper wire, the resistance is",
          copper_wire_resistance(length, gauge), "Ω")
    print("For aluminum wire, the resistance is",
          aluminum_wire_resistance(length, gauge), "Ω")


def diameter(wire_gauge):
    """
    Compute the diameter of a piece of wire from its gauge
    :param wire_gauge: the gauge of the wire
    :return: the diameter of the wire (i mm)
    """
    diam = 0.127 * 92 ** ((36 - wire_gauge) / 39)  # in mm
    return diam / 1000  # in m


def copper_wire_resistance(length, wire_gauge):
    """
    Compute the resistance of a length of copper wire
    :param length: the length of the wire (m)
    :param wire_gauge: the gauge of the wire (AWG)
    :return: the resistance (Ω)
    """
    r = 4 * COPPER_RESISTIVITY * length / (pi * diameter(wire_gauge) ** 2)
    return r


def aluminum_wire_resistance(length, wire_gauge):
    """
    Compute the resistence of a length of aluminum wire
    :param length: the length of the wire (m)
    :param wire_gauge: the gauge of the wire (AWG)
    :return: the resistance (Ω)
    """
    r = 4 * ALUMINUM_RESISTIVITY * length / (pi * diameter(wire_gauge) ** 2)
    return r


# Call the main function.
if __name__== "__main__":
    main()

