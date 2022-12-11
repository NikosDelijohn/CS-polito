from random import randint 
import sys 

def main():

    dice_rolls = [randint(1,6) for _ in range(20)]

    continuous_rolls_max       = -sys.maxsize # max sequence length
    continuous_rolls_max_index_start = None   # starting index of the max sequence 
    
    # We start iterating the list and for EVERY element we launch one extra iteration from 
    # that position towards the end of the list. The nested iteration (while) loop shall stop
    # when either the list bounds have been met, or when continuous values are no more found.    
    for index in range(len(dice_rolls)):

        lookahead_index = index + 1 
        current_continuous_rolls = 0
        while (lookahead_index < len(dice_rolls)-1 and dice_rolls[lookahead_index] == dice_rolls[lookahead_index + 1]):
            current_continuous_rolls += 1
            lookahead_index += 1

        # Note that the comparison > and NOT >= accounts for THE FIRST maximum sequence found
        if current_continuous_rolls > continuous_rolls_max:
            continuous_rolls_max = current_continuous_rolls 
            continuous_rolls_max_index_start = index 

    for index, number in enumerate(dice_rolls):
                
        if index == continuous_rolls_max_index_start:
            print('(',end=' ')
        
        print(number, end= ' ')

        # ')' should be placed in the position given by the starting index + the size of the maximum sequence + 1
        # continous_rolls_max is a counter that can be also used for indexing purposes
        if index == continuous_rolls_max_index_start + continuous_rolls_max + 1:
            print(')',end=' ')

if __name__ == "__main__":
    main()