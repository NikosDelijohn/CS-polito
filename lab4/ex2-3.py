#!/usr/bin/python3

DELTA_T = 0.01
G = 9.81 # m/(s^2)

def main():
    
    v0 = int(input("Write the initial velocity [m/s]: "))
    s0 = 0
    position = s0
    velocity = v0
    position_precise = position
    should_keep_simulating = True
    time_passed = 0
    count = 0

    while should_keep_simulating:

        # precise
        time_passed += DELTA_T
        position_precise = s0 + v0 * time_passed - (1 / 2 * G * time_passed * time_passed)
        # approximated
        velocity = velocity - G * DELTA_T
        position = position + velocity * DELTA_T
        count += 1

        if count % 100 == 0:
            print(f"After {int(count / 100)} seconds...") # not really necessary
            print(f"Precise position: {position_precise}. Approximated position: {position}") # not really necessary
            print(f"Velocity: {velocity}")

        if position_precise <= 0: # if == 0, we might miss it from the simulation!
            should_keep_simulating = False

    print(f"After {count / 100} seconds...")
    print(f"Precise position: {position_precise}. Approximated position: {position}")
    print(f"Velocity: {velocity}")

if __name__ == "__main__":
    main()