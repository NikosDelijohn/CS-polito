# Define constants.
MAX_STARS = 40

def main():
    # Read the data values from the user.
    values = []
    input_str = input("Enter a value (blank to quit): ")
    while input_str != "":
        values.append(float(input_str))
        input_str = input("Enter a value (blank to quit): ")

    # Identify the largest value.
    largest = max(values)

    # Display the bars.
    for i in range(0, len(values)):
        print("*" * round(values[i] / largest * MAX_STARS))

if __name__ == "__main__":

    main()
