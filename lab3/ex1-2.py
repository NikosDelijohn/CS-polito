# Exercise 03.1.2
# Strings identikit

# Read input from the user.
message = input("Enter a string: ")

def main():
    # Check each property and display a message if that property is present.
    if message.isalpha():
        print("The string contains only letters.")

    elif message.isdigit():
        print("The string contains only digits.")

    if message.isalpha() and message.isupper():  # see footnote
        print("All letters in the string are uppercase letters.")

    elif message.isalpha() and message.islower():  # see footnote
        print("All letters in the string are lowercase letters.")

    # Attention: We are using 'if' and not 'elif' in the next section because
    # the following checks are not exclusives

    if message.isalnum():
        print("The string contains only letters and digits.")

    if message[0].isupper():
        print("The string starts with an uppercase letter.")

    if message.endswith("."):
        print("The string ends with a period.")


if __name__ == "__main__":
    main()

# Pay attention to the isupper/islower functions
# The official documentatoin states that the function:
# "Return True if all cased characters in the string are uppercase "
# "and there is at least one cased character, False otherwise"
# This means that the function checks for "all CASED characters", 
# and returns True only if all characters are uppercase. Non-letter 
# characters (e.g. punctuation and spaces) are not checked.
# To check this is necessary to use the function .isalpha(), in order
# to exclude non-alphabetical characters.
# Summing all up, the difference is:
#   - All alphabetical characters are uppercase => .isupper()
#   - All characters are alphabetical and uppercase => .isalpha() and .isupper()
