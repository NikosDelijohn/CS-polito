# Define constant variables.
DISCOUNT_FRACTION = 0.20

def main():
    prices = []
    is_pets = []

    # Read all the prices and pet statuses from the user and store them in
    # two lists.
    price = float(input("Enter the price (-1 to quit): "))
    while price != -1:
        prices.append(price)
        is_pet = input("Is it a pet (Y / N)? ")

        if is_pet.upper() == "Y":
            is_pets.append(True)
        else:
            is_pets.append(False)

        price = float(input("Enter the price (-1 to quit): "))

    # Compute and display the discount amount.
    amount = discount(prices, is_pets, len(prices))
    print("The discount is $%.2f." % amount)


def discount(prices, is_pets, n_items):
    """
    Compute the discount for a transaction

    :param prices: the list of prices
    :param is_pets: the list of True / False values indicating if it is a pet
    :param n_items: the number of items in the transaction
    :return: the amount that should be taken off as a discount
    """
    amount = 0

    # There is only a discount if the user has purchased a pet.
    if True in is_pets:
        # Find all the non-pet items and compute the discount on them.
        for i in range(0, n_items):
            if not is_pets[i]:
                amount = amount + prices[i] * DISCOUNT_FRACTION

    return amount


# Call the main function.
if __name__ == "__main__":

    main()
