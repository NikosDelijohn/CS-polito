#!/usr/bin/python3

def main():

    string_variable = "Mississippi"
    print(f"{string_variable[:3]}...{string_variable[-3:]}")

    less_than_6_chars = "Ghost"
    print(f"{less_than_6_chars[:3]}...{less_than_6_chars[-3:]}")

    less_than_3_chars = "OK"
    print(f"{less_than_3_chars[:3]}...{less_than_3_chars[-3:]}")


if __name__ == "__main__":
    main()