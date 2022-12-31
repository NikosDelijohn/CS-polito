def main():

    # Set up the price chart.
    price_chart = [[10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
                [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
                [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
                [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
                [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
                [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
                [20, 20, 30, 30, 40, 40, 30, 30, 20, 20],
                [20, 30, 30, 40, 50, 50, 40, 30, 30, 20],
                [30, 40, 50, 50, 50, 50, 50, 50, 40, 30]]

    # Read the user's choice.
    choice = input("Pick a (S)eat, Pick a (P)rice or (Q)uit? ").upper()
    while choice != "Q":
        # Handle a seat selection of by seat position.
        if choice == "S":
            row = int(input("Enter the row: "))
            col = int(input("Enter the column: "))
            # Verify that it is still available.
            if price_chart[row][col] != 0:
                print(f"Sold, for {price_chart[row][col]} dollars!")
                price_chart[row][col] = 0
            else:
                print("Sorry, that seat is not available.")
        # Handle a seat selection by price.
        elif choice == "P":
            price = float(input("How much do you want to spend? "))
            found = False

            # Search for a seat with the desired price.
            for row in range(len(price_chart)):
                for col in range(len(price_chart[row])):
                    if price_chart[row][col] == price and not found:
                        print(f"You can have seat ({row}, {col}).")
                        price_chart[row][col] = 0
                        found = True
            if not found:
                print("Sorry, no tickets available at that price.")
        else:
            print("That wasn't a valid option.")

        # Read the next choice.
        choice = input("Pick a (S)eat, Pick a (P)rice or (Q)uit? ").upper()

    # Display the seating map.
    for row in range(len(price_chart)):
        for col in range(len(price_chart[row])):
            print(f"{price_chart[row][col]:3d}", end="")
        print()

if __name__ == "__main__":

    main()