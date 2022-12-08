#!/usr/bin/python3 



def main():

    sequence = list() 

    # fill the sequence 
    while True: 

        user_input = input("Give me an integer number: ")
        while user_input and not user_input.isdigit(): 
            user_input = input("[SANITY CHECK FAILED] Give me an integer number: ")

        if not user_input: 
            break 

        sequence.append(int(user_input))

    # scan for dups 
    duplicates = list() 
    for index in range(len(sequence)-1):

        if (sequence[index] == sequence[index+1]) \
        and(sequence[index] not in duplicates):
            duplicates.append(sequence[index])      

    # report duplicates 
    for dup in duplicates: 
        print(dup,end=" ")
    print()

if __name__ == "__main__":
    main()