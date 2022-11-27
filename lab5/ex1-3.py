#!usr/bin/python3

def main():

    number = input("Give me a number: ")

    while not number.isnumeric():
        number = input("Come on...I said a number!!!: ")
    
    number = int(number) 

    factor = 2
    print("The factors are: ")
    while number > 1: 
        if number % factor == 0: 
            print(factor)
            number = number / factor 

        else:
            factor = factor + 1


if __name__ == "__main__":
    main()