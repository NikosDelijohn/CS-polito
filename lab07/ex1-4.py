import sys

def main():

    user_integers = list()

    user_input = input("Give me a number: ")

    while(len(user_input) != 0 and not user_input.isspace()):

        user_integers.append(int(user_input))

        user_input = input("Give me a number: ")

    local_maxima = list()
    for i in range(1,len(user_integers)-1):

        if user_integers[i-1] < user_integers[i] > user_integers[i+1]:
                local_maxima.append(i)

    if len(local_maxima) == 0:
        exit("There are no local maxima!")
    else:
        print(f"List is {user_integers}")
        print(f"Local maxima found for indices: {local_maxima}")
        
        if len(local_maxima) > 1:

            min_dist = sys.maxsize
            closest_pair = None 
            for index in range(0,len(local_maxima)-1):

                distance = abs(local_maxima[index] - local_maxima[index+1])
                if distance < min_dist:
                    min_dist = distance 
                    closest_pair = (local_maxima[index], local_maxima[index+1])
            
            print(f"Closest pair of local maxima is {closest_pair[0]} - {closest_pair[1]}")



if __name__ == "__main__":
    main()