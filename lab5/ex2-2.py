#!/usr/bin/python3

from random import randint 

UP = 0
DOWN = 1
LEFT = 2 
RIGHT = 3 

def main():

    x = 0 
    y = 0

    for _ in range (100):

        direction = randint(0,4)

        if   direction == UP: y = y + 1 
        elif direction == DOWN: y = y - 1
        elif direction == LEFT: x = x - 1
        elif direction == RIGHT: x = x + 1


    total_distance = abs(x) + abs(y)

    print(f"The drunkard ended up at {x},{y} block")
    print(f"Traveling {total_distance} blocks from 0,0")    

if __name__ == "__main__":
    main()