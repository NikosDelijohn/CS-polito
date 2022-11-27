#!/usr/bin/python3

MAX_TICKETS = 100

def main():

    total_buyers = 0
    available_tickets = MAX_TICKETS 

    while available_tickets > 0: 

        print(f"Available tickets: {available_tickets}")
        
        user_input = int(input("How many tickets you wanna buy?: "))
        while user_input > 4 or user_input > available_tickets or user_input < 1:

            if   user_input < 1: print("You must buy at least 1!")
            elif user_input > 4: print("Maximum 4 tickets per user")
            else: print(f"We have only {available_tickets} left...")

            user_input = int(input("How many tickets you wanna buy?: "))

        available_tickets = available_tickets - user_input
        total_buyers += 1

    print(f"Total unique buyers are {total_buyers}")

if __name__ == "__main__":
    main()