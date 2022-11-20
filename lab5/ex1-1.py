#!/usr/bin/python3

CORRECT_PIN = 1234

def main():

    for i in range(3):

        user_pin = input("What is your PIN?: ")

        # Reminder: We never trust the user input
        #           hence we must sanitize it

        # If the input is NOT numbers only, repeat until it is
        while not user_pin.isnumeric(): 
            user_pin = input("WRONG FORMAT! What is your PIN?: ")

        user_pin = int(user_pin) # Cast string to integer 

        if user_pin == CORRECT_PIN: 
            print("Your PIN is correct")
            exit(0)
        else: 
            print("Your PIN is incorrect")

    print("Your bank card is blocked")
    exit(0)

if __name__ == "__main__":
    main()