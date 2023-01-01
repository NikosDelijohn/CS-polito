#!/usr/bin/python3

PATH_TO_FILE = "text_files/ex1-1/input.txt"

def main():

    try: 

        with open(PATH_TO_FILE) as infile:
            
            for index, line in enumerate(infile.readlines(),start = 1):

                print(f"/*{index}*/{line.rstrip()}")

    except FileNotFoundError:

        exit(f"Tried to open file \"{PATH_TO_FILE}\". It's not found!")

if __name__ == "__main__":

    main()