#!/usr/bin/python3

def shift_right(in_list : list) -> list:

    return [in_list[-1]] + in_list[:-1]

def main():

    integer_list = [4, 1, 7, 9, 3, 0]
    
    print(integer_list, shift_right(integer_list))

if __name__ == "__main__":
    main()