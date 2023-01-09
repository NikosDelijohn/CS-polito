#  Count how many times each word occurs in a file and display the top 5
#  words.


# Read the file name from the user and open the file.
filename = input("Enter the name of a file: ")

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
                        
    except FileNotFoundError:

        exit(f"Tried to open file \"{filename}\". It's not found!")

    # Find the count for the 5th word.
    sorted_counts = sorted(counts.values())
    if len(sorted_counts) < 5:
        count_5 = 1
    else:
        count_5 = sorted_counts[len(sorted_counts) - 5]

    # Display the counts of all words with frequencies above the 5th word.
    count = 0
    for word in sorted(counts):
        if counts[word] > count_5:
            print(f'{word}: {counts[word]}')
            count = count + 1

    # Display enough words with frequency equal to the 5th word so that a total
    # of 5 words are displayed.
    for word in sorted(counts):
        if counts[word] == count_5 and count < 5:
            print(f'{word}: {counts[word]}')
            count = count + 1


if __name__ == "__main__":

    main()