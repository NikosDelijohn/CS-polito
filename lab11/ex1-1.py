#  Count how many times each word occurs in a file.

# Read the file name from the user and open the file.

def main():

    filename = input("Enter the name of a file: ")
    try:

        with open(filename, "r", encoding='utf-8') as inf:
            # Create a new empty dictionary.
            counts = {}

            # Count the words in the file.
            for line in inf:
                words = line.split()
                for word in words:
                    if word in counts:
                        counts[word] = counts[word] + 1
                    else:
                        counts[word] = 1
            # Display the counts.
            for word in sorted(counts):
                print(f"{word}: {counts[word]}")

    except FileNotFoundError:

        exit(f"Tried to open file \"{filename}\". It's not found!")

if __name__ == "__main__":

    main()