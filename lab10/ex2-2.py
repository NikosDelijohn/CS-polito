#!/usr/bin/python3 

FILENAMES_PREFIX = "text_files/ex2-2"

def main():

    # Read the student id from the user.
    sid = input("Enter the student id: ")

    try: 

        with open(f"{FILENAMES_PREFIX}/classes.txt") as course_file: 

            courses = [x.rstrip() for x in course_file]
       

    except FileNotFoundError: 

        exit(f"Tried to open file \"{FILENAMES_PREFIX}/classes.txt\". It's not found!")

    print(f"Student ID:  {sid} \n")

    for course in courses:

        try: 

            with open(f"{FILENAMES_PREFIX}/{course}.txt") as course_results: 

                for line in course_results: 

                    if sid in line: print(f"{course} {line.split()[-1]}")

        except FileNotFoundError:

            exit(f"Tried to open file \"{FILENAMES_PREFIX}/{course}\". It's not found!")


if __name__ == "__main__":
    
    main()