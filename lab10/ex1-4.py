#!/usr/bin/python3 

PATH_TO_FILE = "text_files/ex1-4/input.txt" 

def main():

    try: 

        with open(PATH_TO_FILE) as infile: 

            entries = { index : x.rstrip().split(';') for index, x in enumerate(infile.readlines()) }

    except FileNotFoundError:

        exit(f"Tried to open file \"{PATH_TO_FILE}\". It's not found!")

    
    # dict of type "service_type" : "total_amount"
    services = dict()

    for entry in entries:
        
        service     = entries[entry][1]
        amount      = entries[entry][2]

        if service in ["Conference","Lodging","Dinner"] and service not in services.keys(): 

            services[service] = 0

        elif service not in ["Conference","Lodging","Dinner"]: 

            exit(f"Invalid service ({service}) for entry {entries[entry]}")

        
        try: 

            amount = float(amount) 

        except ValueError:

            exit(f"Invalid format amount paid ({amount}) for entry {entries[entry]}")

        services[service] += amount 

    for service, total_value in services.items(): 

        print(f"{service}: total = {total_value}")


if __name__ == "__main__":
    main()