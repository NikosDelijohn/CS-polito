#!/usr/bin/python3

A = 32_310_901 
B = 1_729
M = 224

def main(): 

    seed = int(input("Give me an initial value: "))

    r_old = seed 
    for _ in range(100):
        r_new = (A * r_old + B) % M
        r_old = r_new 

        print(r_new)

if __name__ == "__main__":
    main()