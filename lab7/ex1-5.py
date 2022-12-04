#!/usr/bin/python3


def same_set(a : list, b : list) -> bool:  

    for elem in a: 
        
        if elem not in b: 
   
            return False 
        
    for elem in b: 

        if elem not in a: 
   
            return False 

    return True 


def main():

    first_list = [ 1, 4, 9, 16, 9, 7, 4, 9, 11 ]
    second_list = [ 11, 11, 7, 9, 16, 4, 1 ]

    print(same_set(first_list,second_list))

    

if __name__ == "__main__":
    main()