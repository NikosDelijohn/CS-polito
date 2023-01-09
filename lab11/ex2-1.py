#  Read a database of per capita income by country and allow the user to
#  query it.

def main():

    # Load the data into a dictionary.
    incomes = {}
    try:

        with open("rawdata_2004.txt", "r", encoding='utf-8') as inf:
            for line in inf:
                parts = line.split("\t")

                # Remove the dollar sign and comma.
                parts[2] = parts[2].replace("$", "")
                parts[2] = parts[2].replace(",", "")

                # Add the country to the dictionary.
                incomes[parts[1].upper()] = float(parts[2])

            # Read queries from the user and respond to them.
            country = input("Enter a country name (or type quit to quit): ").upper()
            while country != "QUIT":
                if country in incomes:
                    print("The per capita income is", incomes[country])
                else:
                    print("That wasn't a recognized country.")
                print()

                # Read the next country from the user.
                country = input("Enter a country name (or type quit to quit): ").upper()

    except FileNotFoundError:
        exit(f"Tried to open file rawdata_2004.txt. It's not found!")

if __name__ == "__main__":

    main()