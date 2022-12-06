#!/usr/bin/python3 

"""
PSEUDOCODE:
 
1.  Store the cost of the car into a variable from the user. 
2.  Store the kilometers traveled per year into a variable.
3.  Store the estimate cost of fuel into a variable from the user.
4.  Store the efficiency in kilometers per liter from the user.
5.  Store the estimate of the resale value of the car in 5 years from the user.
6.  Calculate fuel the car will need for 5 years: fuel_needed = 5 * (kilometers_per_year / kilometers_per_liter)
7.  Calculate the total fuel cost: total_fuel_cost = fuel_needed * fuel_cost 
8.  Calculate the total cost: total_cost = initial_cost + total_fuel_cost - resale_value
9. Print the total cost for 5 years
"""

# underscore is used to separate the thousands for readability purposes
KILOMETERS_PER_YEAR = 30_000 # 2.
# the above statement is exactly equal to KILOMETERS_PER_YEAR = 30000  

def main():

    initial_cost = int(input("Car's initial cost (in €): "))              # 1.
    cost_of_fuel = int(input("Cost of fuel (in €): "))                    # 3.
    km_per_liter = int(input("Kilometers per liter: "))                   # 4.
    resale_value = int(input("Car's resale value in 5 years (in €): "))   # 5.
 
    fuel_needed = 5 * (KILOMETERS_PER_YEAR / km_per_liter )               # 6.
    total_fuel_cost = fuel_needed * cost_of_fuel                          # 7.
     
    car_total_cost = initial_cost + total_fuel_cost - resale_value        # 8.

    print(f"The total cost of the car for 5 years is {car_total_cost}€.") # 9.

if __name__ == "__main__":
    main()