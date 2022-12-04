# Exercise 03.2.9
# Wavelengths

def main():
    #  Display the description of some radiation given its wavelength.

    # Read input from the user.
    wavelength = float(input("Enter the wavelength: "))

    # Display the description of the radiation.
    if wavelength > 1e-1:
        print("Radio Waves")
    elif wavelength > 1e-3:
        print("Microwaves")
    elif wavelength > 7e-7:
        print("Infrared")
    elif wavelength > 4e-7:
        print("Visible Light")
    elif wavelength > 1e-8:
        print("Ultraviolet")
    elif wavelength > 1e-11:
        print("X-rays")
    else:
        print("Gamma rays")

if __name__ == "__main__":
    main()
