#!/usr/bin/python3 

PLAYER = 0
CPU = 1
SMART = 0
DUMB = 1

import random

def main():

    num_marbles = random.randint(10, 100)
    first_move = random.choice([PLAYER, CPU])
    strategy = random.choice([SMART, DUMB])
    strategy = SMART
    loser = -1 # using an invalid value, easy comparison
    current_player = first_move

    print(f"Marbles: {num_marbles}")

    while loser < 0:
        if current_player == PLAYER:
            # Player's turn
            print("It's on you, player!")
            ok = False
            while not ok:
                marbles_str = input("Take a number of marbles: ")
                if marbles_str.isdigit() and int(marbles_str) <= num_marbles / 2 and int(marbles_str) > 0:
                    num_marbles -= int(marbles_str)
                    ok = True
            current_player = CPU # change player

        elif current_player == CPU:
            # CPU's turn
            print("It's the CPU turn now...")
            marbles_to_take = 0

            if strategy == DUMB:
                marbles_to_take = random.randint(1, int(num_marbles / 2))
            else:
                # find the best number
                best_remaining = 2
                while num_marbles - (best_remaining - 1) > int(num_marbles / 2):
                    best_remaining *= 2
                best_remaining -= 1
                marbles_to_take = num_marbles - int(best_remaining)
                if best_remaining >= num_marbles: # we did not find a feasible number
                    marbles_to_take = random.randint(1, int(num_marbles / 2))
            num_marbles -= marbles_to_take
            current_player = PLAYER # change player

        print(f"Marbles left: {num_marbles}")

        if num_marbles == 1:
            loser = current_player

    if loser == CPU:
        print("The CPU lost.")
        
    elif loser == PLAYER:
        print("The player lost.")


if __name__ == "__main__":
    main()