#!/usr/bin/python3

def main():

    word = input("Write a word here: ")
    for num_chars in range(len(word)):
        for i in range(len(word) - num_chars):
            substring = ""
            for chars in range(i, i + num_chars + 1):
                substring += word[chars]
            print(substring)


if __name__ == "__main__":
    main()