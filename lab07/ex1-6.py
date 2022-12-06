#!/usr/bin/python3

from random import randint 

def main():

    randomized_list = [ randint(0,99) for _ in range(20) ]

    for elem in randomized_list: print(elem, end=' ')

    print('\n-- sorted -- ')

    randomized_list.sort() 

    for elem in randomized_list: print(elem, end=' ')

if __name__ == "__main__":
    main()