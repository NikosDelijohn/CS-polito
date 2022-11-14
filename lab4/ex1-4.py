#!/usr/bin/python3

def main():

    word = input("Write a word here: ")
    string_reverse = ""
    uppercase_reverse = ""
    index = len(word) - 1

    for index in range(len(word) - 1, -1, -1):
        string_reverse += word[index]
        if word[index] >= 'A' and word[index] <= 'Z':
            uppercase_reverse += word[index]

    print(string_reverse)
    print(uppercase_reverse)

if __name__ == "__main__":
    main()