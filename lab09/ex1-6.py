def main():
    
    sequence = input("Insert a sequence of numbers (separated by ':') = ")

    values = sequence.split(':')
    for i in range(len(values)):
        values[i] = int(values[i])

    # find and delete min and max
    copy = list(values)
    val_min = min(copy)
    copy.remove(val_min)
    val_max = max(copy)
    copy.remove(val_max)

    for i in range(len(copy)):
        copy[i] = str(copy[i])
    print(':'.join(copy))

    # only even numbers
    copy = []
    for val in values:
        if val % 2 == 0:
            copy.append(val)

    for i in range(len(copy)):
        copy[i] = str(copy[i])
    print(':'.join(copy))

    # only 2-digit numbers
    copy = []
    for val in values:
        if 10 <= val <= 99:
            copy.append(val)

    for i in range(len(copy)):
        copy[i] = str(copy[i])
    print(':'.join(copy))

if __name__ == "__main__":

    main()