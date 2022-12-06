#!/usr/bin/python3 

def main():
   
    ok = True
    found_equals = False
    prev = -1
    repeated = ""

    while ok:
        line = input("Write a number: ")
        if line == "":
            ok = False
        else:
            if not line.isdigit():
                print("This should be a number!")
            else:
                num = int(line)
                if num == prev:
                    found_equals = True
                if num != prev and found_equals == True:
                    repeated += f"{prev} "
                    found_equals = False
                prev = num
    print(repeated)


if __name__ == "__main__":
    main()