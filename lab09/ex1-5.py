# Define constants.
MAX_STARS = 40

def main():

    # Read the data values from the user.
    values = []
    labels = []
    label = input("Enter the label: ")
    while label != "":
        labels.append(label)
        values.append(float(input("Enter the value " + label + ": ")))
        label = input("Enter the label: ")

    # Identify the largest value.
    largest = max(values)

    # Display the bars.
    for i in range(0, len(values)):
        print("%15s %s" % (labels[i], "*" * round(values[i] / largest * MAX_STARS)))

if __name__ == "__main__":

    main()
