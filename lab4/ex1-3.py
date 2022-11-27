#!/usr/bin/python3 

def main():

    n = int(input("Provide the side length of the shape: "))

    # square, solution 1
    x = 0
    y = 0
    while y < n:
        while x < n:
            print("*", end="")
            x += 1
        print("")
        y += 1
        x = 0
    print("")

    # square, solution 2
    x = 0
    y = 0
    square = ""
    while y < n:
        while x < n:
            square += "*"
            x += 1
        square += "\n"
        y += 1
        x = 0
    print(square)

    # square, solution 3
    y = 0
    while y < n:
        print("*" * n)
        y += 1
    print("")

    # rhombus
    diagonal_len = n * 2 - 2
    y = 0
    while y < n:
        shape_begin = int(diagonal_len / 2) - y 
        shape_end = int(diagonal_len / 2) + y
        x = 0
        while x <= shape_end:
            if x < shape_begin:
                print(" ", end="")
            else:
                print("*", end="")
            x += 1
        print("")
        y += 1
    while y <= diagonal_len:
        shape_begin = int(diagonal_len / 2) - (diagonal_len - y)
        shape_end = int(diagonal_len / 2) + (diagonal_len - y)
        x = 0
        while x <= shape_end:
            if x < shape_begin:
                print(" ", end="")
            else:
                print("*", end="")
            x += 1
        print("")
        y += 1
    print("")

if __name__ == "__main__":
    main()

# challenge: do it printing only once
