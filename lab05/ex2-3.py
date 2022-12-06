#!/usr/bin/python3

def main():

    A = float(input("Give me the initial value for A: "))
    B = float(input("Give me the initial value for B: "))
    C = float(input("Give me the initial value for C: "))
    D = float(input("Give me the initial value for D: "))

    prey = int(input("Enter the initial prey (1000 is a good choice): "))
    predators = int(input("Enter the initial predators (20 is a good choice): "))

    iterations = int(input("How many iterations?: "))

    for period in range (1, iterations + 1):

        new_prey = prey * (1+A - B*predators)
        new_predators = predators * (1-C + D*prey)

        if round(new_prey) !=0 and round(new_predators) !=0: 
            print(f"[PERIOD #{period:4}]: Predators := {round(new_predators)} vs Prey := {round(new_prey)}")

        if round(new_prey) == 0:
            print(f"Prey has been eliminated...RIP")
            exit(0)
        elif round(new_predators) == 0:
            print(f"Predators have been eliminated...Hooray!")
            exit(0) 

        prey = new_prey
        predators = new_predators 

if __name__ == "__main__":
    main()