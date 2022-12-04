# Exercise 03.1.3
# Strings and substrings

def main():

    long_sequence = input("Insert a 'long' DNA sequence: ")

    # Convert to uppercase for easier manipulation
    long_sequence = long_sequence.upper()

    # To verify that long_sequence contains ONLY the 4 letters ACTG
    # we need to use cycle, so we don't do this here

    short_sequence = input("Insert a 'short', 3 letter DNA sequence: ")
    short_sequence = short_sequence.upper()

    if len(short_sequence) != 3:
        print('Errore: short_sequence must contain exactly 3 letters')
        exit()

    # verify if short_sequence is in long_sequence

    found = long_sequence.find(short_sequence)
    if found == -1:
        print('Short sequence is not present in long sequence')
    else:
        print('Short sequence is present starting from positon', found)

        # verify how many times the short sequence is inside the long sequence
        # (This needs to be done only if the short sequence is in the long sequence)
        number_of_repetitions = long_sequence.count(short_sequence)
        print('Sequence', short_sequence, 'appears', number_of_repetitions, 'time(s)')

if __name__ == "__main__":
    main()