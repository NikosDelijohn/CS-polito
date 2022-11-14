# Exercise 03.2.7
# Conversion

# Read the unit to convert from and to.

from_unit = input("Convert from? (ml, l, g, kg, mm, cm, m, km): ")
to_unit = input("Convert to? (fl. oz, gal, oz, lb, in, ft, mi): ")

# Volume units.
if from_unit == "ml" and to_unit == "fl. oz":
    factor = 0.03381406
elif from_unit == "l" and to_unit == "fl. oz":
    factor = 33.81405650
elif from_unit == "ml" and to_unit == "gal":
    factor = 0.00026417
elif from_unit == "l" and to_unit == "gal":
    factor = 0.26417218

# Weight / mass units.
elif from_unit == "g" and to_unit == "oz":
    factor = 0.03527399
elif from_unit == "kg" and to_unit == "oz":
    factor = 35.27399072
elif from_unit == "g" and to_unit == "lb":
    factor = 0.00220462
elif from_unit == "kg" and to_unit == "lb":
    factor = 2.20462442

# Distance units.
elif from_unit == "mm" and to_unit == "in":
    factor = 0.03937008
elif from_unit == "cm" and to_unit == "in":
    factor = 0.39370079
elif from_unit == "m" and to_unit == "in":
    factor = 39.37007874
elif from_unit == "km" and to_unit == "in":
    factor = 39370.07874016
elif from_unit == "mm" and to_unit == "ft":
    factor = 0.00328084
elif from_unit == "cm" and to_unit == "ft":
    factor = 0.03280840
elif from_unit == "m" and to_unit == "ft":
    factor = 3.28083990
elif from_unit == "km" and to_unit == "ft":
    factor = 3280.83989501
elif from_unit == "mm" and to_unit == "mi":
    factor = 0.00000062
elif from_unit == "cm" and to_unit == "mi":
    factor = 0.00000621
elif from_unit == "m" and to_unit == "mi":
    factor = 0.00062137
elif from_unit == "km" and to_unit == "mi":
    factor = 0.62137119
# Incompatible units.
else:
    exit("Those units are not compatible.")

# Read the value to convert from the user.
value = float(input("Value? "))

# Compute the result.
result = value * factor

# Display the result.
print(value, from_unit, "=", result, to_unit)
