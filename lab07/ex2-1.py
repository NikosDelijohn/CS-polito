
def custom_filter(list_ : list) -> list: 

    average = lambda ints : sum(ints)/len(ints)

    old_left = None  

    for i in range(len(list_)):
        
        if i == 0: 
            old_left = list_[i]
            list_[i] = average( [list_[i],list_[i+1]] )

        elif i == len(list_)-1: 
            list_[i] = average( [old_left, list_[i] ] )

        else: 
            current = list_[i]
            list_[i] = average( [old_left, list_[i], list_[i+1]] )
            old_left = current

    return list_
    
def main():

    test_case = [1,2,3,4,5,6,7,8,9]

    print(custom_filter(test_case))

if __name__ == "__main__":
    
    main()