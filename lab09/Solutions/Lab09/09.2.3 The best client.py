# Exercise 09.2.3
# The best client

#  Display the best customer of the day.

def main():
    sales = []
    names = []

    # Read the names and sales amounts, storing them in two lists.
    amount = float(input("Enter the sale amount: "))
    while amount != 0:
        sales.append(amount)

        name = input("Enter the customer's name: ")
        names.append(name)

        amount = float(input("Enter the sale amount: "))

    # Compute and display the name of the best customer.
    best_name = name_of_best_customer(sales, names)
    print("The best customer was:", best_name)


def name_of_best_customer(sales, customers):
    """
    Identify the name of the best customer
    :param sales: the list of sale amounts
    :param customers: the names of the customers
    :return: the name of the customer with the highest sale amount
    """
    # Find the largest sale.
    largest = max(sales)

    # Display the name of the best customer.
    # If more than one has the same sales, return the 1st one
    for i in range(len(sales)):
        if sales[i] == largest:
            return customers[i]

    # Alternate solution
    # return customers[sales.index(max(sales))]


# Call the main function.
main()
