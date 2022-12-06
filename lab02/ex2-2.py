#!/usr/bin/python3

def main():

    telephone_number = input("Give me a 10-digit telephone number: ")

    print(f"({telephone_number[:3]}) {telephone_number[3:6]}-{telephone_number[6:]}")

if __name__ == "__main__":
    main()