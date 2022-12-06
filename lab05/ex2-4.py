#!/usr/bin/python3

R0 = 20
VS = 40
RS = 8 

def main():

    max_power = -1 
    max_turns = -1 

    n = 0.01
    while n <= 2.0: 
        Ps = RS * ((n * VS) / (n * n * R0 + RS)) ** 2

        if Ps > max_power: 
            max_power = Ps 
            max_turns = n 
        
        n += 0.01
    
    print(f"The maximum power is {max_power:.3f} with turns ratio of {max_turns:.3f}")

if __name__ == "__main__":
    main()