#!/usr/bin/python3 

def main():
    
    erroneous_attempts = 0
    float_sum          = 0

    user_input = input(f"[ERRORS {erroneous_attempts}]> ")

    while True: 

        if not user_input: 
            break 

        try: 
            user_input = float(user_input) 
            float_sum += user_input

        except ValueError: 
            print(f"Invalid format for float ({user_input}). ")

            if erroneous_attempts == 2: 
                exit("Aborting...")

            else:
                erroneous_attempts += 1
        

        user_input = input(f"[ERRORS {erroneous_attempts}]> ")

    print(f"Sum: {float_sum}")


if __name__ == "__main__":
    main() 