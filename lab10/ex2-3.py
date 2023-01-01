#!/usr/bin/python3 

FILENAME_PREFIX = "text_files/ex2-3/"

def main():

    # Gather input from the user.
    keyword = remove_duplicates(input("Enter the keyword: ").upper())
    in_name = input("Enter the input file name: ")
    out_name = input("Enter the output file name: ")

    # Read all the text from the file.
    try:

        in_file = open(f"{FILENAME_PREFIX}/{in_name}", "r", encoding='utf-8')
    
    except FileNotFoundError: 

        exit(f"Tried to open file \"{FILENAME_PREFIX}/{in_name}\". It's not found!")

    text = in_file.read()
    in_file.close()

    # I's and J's are considered the same, so replace all J's with I's.
    text = text.replace("J", "I").replace("j", "i")

    # Ensure we have an even number of letters by padding with a Z.
    count = 0
    for ch in text:
        if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            count = count + 1

    if count % 2 == 1:
        text = text + "Z"

    # I's and J's are considered the same, so replace all J's with I's.
    keyword = keyword.replace("J", "I")

    # Create the table for modifying the text.
    table = create_table(keyword)

    # Perform the transformation.
    result = ""
    i = 0
    while i < len(text):
        before = ""
        between = ""
        after = ""

        while i < len(text) and not text[i].isalpha():  # the condition skips to the next alphabetic character
            before = before + text[i]
            i = i + 1

        (r1, c1) = get_pos(text[i], table)
        i = i + 1

        while i < len(text) and not text[i].isalpha():
            between = between + text[i]
            i = i + 1

        (r2, c2) = get_pos(text[i], table)
        i = i + 1

        while i < len(text) and not text[i].isalpha():
            after = after + text[i]
            i = i + 1

        # Handle two letters in the same row.
        if r1 == r2:
            result = result + before + table[r1][c2] + between + table[r2][c1] + after
        # Handle two letters in the same column.
        elif c1 == c2:
            result = result + before + table[r2][c2] + between + table[r1][c1] + after
        # Handle the general case.
        else:
            result = result + before + table[r1][c2] + between + table[r2][c1] + after

    # Save the result.
    try: 

        out_file = open(f"text_files/ex2-3/{out_name}", "w", encoding='utf-8')
    
    except OSError:
        
        exit(f"Something went wrong while trying to create output file ({FILENAME_PREFIX}/{out_name}).")
  
    out_file.write(result)
    out_file.close()


def get_pos(letter, table):
    """
    Find the row and column in which a letter exists in a table

    :param letter: the letter to search for
    :param table: the table to search
    :return: the row and column in which letter resides, or (-1, -1) if not found
    """
    for row in range(len(table)):
        for col in range(len(table[row])):
            if table[row][col] == letter.upper():
                return (row, col)
    return (-1, -1)


def create_table(keyword):
    """
    Create the 5x5 table for a playfair cipher.

    :param keyword: the keyword used to construct the table with no duplicates
    :return: the 5x5 encryption table
    """
    # Generate an empty table.
    table = []
    for i in range(0, 5):
        table.append([0] * 5)

    # Generate all the letters to go in the table in the correct order.
    all_letters = keyword
    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # note: the J is missing
        if ch not in all_letters:
            all_letters = all_letters + ch

    # Copy the letters into the table.
    for row in range(0, 5):
        for col in range(0, 5):
            table[row][col] = all_letters[row * 5 + col]

    # Return the result.
    return table


def remove_duplicates(s):
    """
    Create a new version of a string containing no duplicate letters.

    :param s: the string to remove duplicate letters from
    :return: a new string where all duplicate letters have been removed
    """
    retval = ""
    for ch in s:
        if ch not in retval:
            retval = retval + ch
    return retval


# Call the main function.
if __name__ == "__main__":

    main()