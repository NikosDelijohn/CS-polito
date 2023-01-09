#  Count how many times each word occurs in a file.

# Read the file name from the user and open the file.

PATH_TO_FILE = "input_file/ex1-1/input.txt"

def main():

    filename = input("Enter the name of a file: ")
    try:

        with open(PATH_TO_FILE, "r", encoding='utf-8') as inf:
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

    except FileNotFoundError:

        exit(f"Tried to open file \"{filename}\". It's not found!")

    # Display the counts.
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")

if __name__ == "__main__":

    main()