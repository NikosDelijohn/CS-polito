#!/usr/bin/python3

from random import randint

def main():

    random_ints = [ randint(1,100) for _ in range(100) ]

    print("Initial list")
    for x in random_ints: print(x, end=' ') 

    # I 
    print("All elements of even index:")
    for index, number in enumerate(random_ints):

        if index % 2 == 0: 

            print(number, end=' ')
    
    # II 
    print("All elements of even value:")
    for number in random_ints:

        if number % 2 == 0: 
            print(number, end=' ')

    # III 
    print("All elements in reverse order:")
    random_ints.reverse()

    for number in random_ints: 
        print(number, end=' ')

    # IV
    # Note that for the first I am printing the last because the .reverse() has changed the order 
    # of the initial list!!!!
    print("The first and the last element") 
    print(f"First = {random_ints[-1]}\nLast  = {random_ints[0]}")

if __name__ == "__main__":
    main()