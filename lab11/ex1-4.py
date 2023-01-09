#  Implement a censor that replaces "bad" words with asterisks.

# Read the bad words into a set.

FILENAMES_PREFIX = "input_files/ex1-4"

def main():

    try:

        with open(f"{FILENAMES_PREFIX}/bad_words.txt", "r", encoding='utf-8') as bad_file:
            bad_words = set()
            for word in bad_file:
                word = word.rstrip()
                bad_words.add(word)

    except FileNotFoundError:

        exit(f"Tried to open file {FILENAMES_PREFIX}/bad_words.txt. It's not found!")

    # Read the input file and store it in a set.
    input_name = input("Enter the input file name: ")
    output_name = input("Enter the output file name: ")

    try:
        with open(f"{FILENAMES_PREFIX}/{input_name}", "r", encoding='utf-8') as inf, open(f"{FILENAMES_PREFIX}/{output_name}", "w", encoding='utf-8') as outf:
            # Censor the input file, writing the result to the output file.
            for line in inf:
                for bad_word in bad_words:
                    # Check each position in the line.
                    for pos in range(0, len(line) - len(bad_word)):
                        # If we found the word at that position.
                        if line[pos: pos + len(bad_word)].upper() == bad_word.upper():
                            # Verify that it is actually a word, and not just part of another
                            # word.
                            if (pos == 0 or line[pos - 1] == " ") and \
                                    (pos + len(bad_word) == len(line) - 1 or line[pos + len(bad_word)] in " .,;:?!"):
                                # Perform the replacement.
                                line = line[: pos] + "*" * len(bad_word) + line[pos + len(bad_word):]

                # Write the line to the output file.
                outf.write(line)
    except OSError:
        exit(f"Tried to open file \"{input_name}\" and \"{output_name}\". Something went wrong there.")


if __name__ == "__main__":

    main()
