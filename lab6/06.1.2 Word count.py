# Excersice 06.1.2
# Word count

"""
Use a function to count the number of words in a string.
"""


def main():
    input_str = input("Enter a string: ")
    print("The string contains", count_words(input_str), "words")
    # print("The string contains", count_words_using_split(input_str), "words")


def count_words(string):
    """
    Count the number of words in a string.
    *Warning*: words must be separated by **one** space, only.

    :param string: the string of characters to process
    :return: the number of words
    """

    # Remove any leading or trailing spaces to make counting easier.
    string = string.strip()

    # Handle the empty string as a special case.
    if string == "":
        return 0

    # Count the spaces to count the number of words.
    # Words = Spaces + 1 (therefore, initialize count to 1)
    count = 1
    for ch in string:
        if ch == " ":
            count = count + 1

    # Alternative solution using the .count() method for strings:
    # count = string.count(' ') + 1
    return count


def count_words_using_split(string):
    """
    Alternative solution to count the number of words in a string by using split().

    :param string: the string of characters to process
    :return: the number of words
    """
    # Split a string into a list and return the number of elements in that list
    return len(string.split())


# Call the main function.
main()
