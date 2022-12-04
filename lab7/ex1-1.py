#!/usr/bin/python3

def get_valid_digit() -> str:

    retval = input(">Give me a number: ")

    while not retval.isdigit() and retval != "": 
        retval = input(">Give me a valid number: ")

    return retval 


def main():

    numbers = list() 

    num = get_valid_digit()
    while num: 
        numbers.append(num)
        num = get_valid_digit()
    
    if len(numbers) == 0: 
        exit("Zero numbers provided")
    
    # https://docs.python.org/3/library/functions.html#map
    numbers = list(map(int, numbers))

    alternating_sum = 0
    output_string = str(numbers[0])
    for index, number in enumerate(numbers):

        # https://www.geeksforgeeks.org/ternary-operator-in-python/
        alternating_sum +=  number if (index % 2 == 0) else - number 
        
        if index > 0:
            output_string +=  f" + {str(number)}" if (index % 2 == 0) else f" - {str(number)}"
    
    output_string += f" = {alternating_sum}"

    print(output_string)


if __name__ == "__main__":
    main()