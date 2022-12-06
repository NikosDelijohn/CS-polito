#!/usr/bin/python3

VOWELS = "AEIOU"
MASCULINE_EXCEPTIONS = ["Belize", "Cambodge", "Mexique", "Mozambique", "Zaïre", "Zimbambwe"]
PLURAL_EXCEPTIONS = ["Etats-Unis", "Pays-Bas"]

def main():

    while True: 

        user_input = input("Give me a country name: ")

        # Country names must always start with a capital letter!
        while user_input[0].islower(): 
            user_input = input("Country names start with capital letters! Try again: ")

        if user_input in MASCULINE_EXCEPTIONS: 
            print(f"le {user_input}")

        elif user_input in PLURAL_EXCEPTIONS:
            print(f"les {user_input}")

        elif user_input[0] in VOWELS:
            print(f"l' {user_input}")

        elif user_input[-1] == "e":
            print(f"la {user_input}")

        else:
            print(f"le {user_input}")
        
        user_input = input("Continue? [Y/N]: ")
        if user_input == 'n' or user_input == 'N': 
            exit(0)


if __name__ == "__main__":
    main()