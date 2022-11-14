#!/usr/bin/python3

VOWELS = "AEIOUYaeiouy"

def main():

    line = input("Write a line: ")
    index = 0
    only_capitals = ""
    only_even_positions = ""
    without_vowels = ""
    num_digits = 0
    vowel_positions = ""

    for index in range(len(line)):
        if line[index] >= 'A' and line[index] <= 'Z':
            only_capitals += line[index]
        if index % 2 == 0:
            only_even_positions += line[index]
        if line[index] in VOWELS:
            without_vowels += "_"
            vowel_positions += f"{index} "
        else:
            without_vowels += line[index]
        if line[index] >= '0' and line[index] <= '9':
            num_digits += 1

    print(f"Original input: {line}")
    print(f"Only capital letters: {only_capitals}")
    print(f"Only even positions: {only_even_positions}")
    print(f"With replaced vowels: {without_vowels}")
    print(f"Number of digits in the string: {num_digits}")
    print(f"Positions of the vowels: : {vowel_positions}")

if __name__ == "__main__":
    main()