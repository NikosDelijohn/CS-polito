#  Display the characters that occur in both strings, occur in one string
#  but not the other, and that don't occur in either string.

# Gather input from the user and store them as sets.

def main():

    set1 = set(input("Enter the first string: ").upper())
    set2 = set(input("Enter the second string: ").upper())

    # Find and display the characters common to both strings.
    common = set1.intersection(set2)
    print("The characters that are in both strings:")
    for ch in sorted(common):
        print(ch, end=" ")
    print()

    # Find and display the characters in string 1 but not string 2.
    diff = set1.difference(set2)
    print("The characters in string 1 that are not in string 2:")
    for ch in sorted(diff):
        print(ch, end=" ")
    print()

    # Find and display the characters that are not in either string.
    all_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    print("The letters that are not in either string:")
    neither = all_chars.difference(set1.union(set2))
    for ch in sorted(neither):
        print(ch, end=" ")
    print()

if __name__ == "__main__":

    main()