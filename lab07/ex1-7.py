from importlib import import_module

# another way of importing my own package 
my_package = import_module("ex1-3")

def main():

    test_my_list = [1,1,1,1,2,3,4,5]
    
    print(sum(my_package.remove_min(test_my_list)))



if __name__ == "__main__":
    main()
