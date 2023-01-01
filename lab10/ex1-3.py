#!/usr/bin/python3

FILENAMES_PREFIX = "text_files/ex1-3"

def main():

    user_input_files = input("Give me the filenames (comma separated): ")

    files = [ f"{FILENAMES_PREFIX}/{x}" for x in user_input_files.rstrip().split(',')] 

    user_input_word = input("Keyword?: ")

    found_lines = list() 

    for file_ in files:

        try: 

            with open(file_) as infile: 

                for line in infile.readlines():

                    if user_input_word in line: 
                        # file_ = FILENAMES_PREFIX/filename so we need to trim it down for 
                        # showing only the filename and to omit the relative path hence the split on '/'
                        found_lines.append(f"{file_.split('/')[-1]}: {line.rstrip()}")

        except FileNotFoundError: 

            exit(f"Tried to open file \"{FILENAMES_PREFIX}/{file_}\". It's not found!") 

    for line in found_lines:
        print(line)


if __name__ == "__main__":
    main()