#!/usr/bin/python3

PATH_TO_FILE = "text_files/ex2-4/input.txt"

def main():
    
    try: 

        with open(PATH_TO_FILE) as infile: 

            lines = infile.readlines()

    except FileNotFoundError: 

        exit(f"Tried to open file \"{PATH_TO_FILE}\". It's not found!")

    # Search the data until the user enters a blank line.
    search = input("What do you want to look for (blank to quit)? ")
    while search != "":
        # Find all lines that match the search value and display the other values.
        for line in lines:
            parts = line.split()
            if search.upper() in parts[0].upper():
                print("Bond Energy:", parts[1], "  Bond Length:", parts[2])
            if search in parts[1]:
                print("Bond Type:", parts[0], "  Bond Length:", parts[2])
            if search in parts[2]:
                print("Bond Type:", parts[0], "Bond Energy:", parts[1])

        # Read the next input from the user.
        print()
        search = input("What do you want to look for (blank to quit)? ")

if __name__ == "__main__":
    main()