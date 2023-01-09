#!/usr/bin/python3

FILENAMES_PREFIX = "input_files/"

def extract_fruit(sentence : str) -> str: 
    
    tokens = sentence.split()

    return "".join([x for x in tokens if x.isupper()])

def main():

    filename = input(">filename? ")

    alice_backpack = dict() 

    try: 

        with open(f"{FILENAMES_PREFIX}/{filename}") as infile: 

            entries = [ x.rstrip() for x in infile.readlines() ]

    except OSError:

        exit(f"Could not open file {filename}")

    
    for line in entries:

        fruit = extract_fruit(line)
        name  = line.split()[0]

        # Bob gives to Alice something 
        if name == "Bob":

            if len(alice_backpack) > 42: 
                
                exit(f"Alice backpack exceeds capacity of 42 for line \"{line}\"")

            alice_backpack[fruit] = 1 if fruit not in alice_backpack else alice_backpack[fruit] + 1
                

        elif name == "Carl":

            if fruit not in alice_backpack:
                
                exit(f"Carl tries to take a fruit {fruit} that does not exist in Alice's backpack.")

            alice_backpack[fruit] -= 1

            # if there are no more fruits of this type 
            # delete the entry from the dict to free up 
            # space for future insertions
            if alice_backpack[fruit] == 0: 
                
                del alice_backpack[fruit]


    print(f"Transactions completed without an error!")

if __name__ == "__main__":

    main()