#!/usr/bin/python3

import sys 

def remove_min(list_ : list) -> list: 

    min_ = sys.maxsize  
    for index, number in enumerate(list_): 

        if number < min_: 
            min_ = number 

    #https://docs.python.org/3/library/functions.html#filter
    return list(filter(lambda x : x != min_, list_))

def main():

    test_case = [1,2,3,-5,-5,-5,4,5,6]
    print(test_case)
    print(remove_min(test_case))


if __name__ == "__main__":
    main()