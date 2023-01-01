#!/usr/bin/python3

PATH_TO_FILE = "text_files/ex1-2/input.txt"

def main():

    try: 

        with open(PATH_TO_FILE) as infile: 

            lines = [ x.rstrip() for x in infile.readlines() ]

    except FileNotFoundError: 

        exit(f"Tried to open file \"{PATH_TO_FILE}\". It's not found!")


    lines.reverse()

    for line in lines: 

        print(line)

if __name__ == "__main__":

    main()