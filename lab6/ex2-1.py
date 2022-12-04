# Excercise 06.2.1
# ONG

"""
Compute the financial assistance for needy families.
"""


def main():
    # Read income values from the user until -1 is entered.
    income = float(input("What is the household income (-1 to quit)? "))
    while income != -1:
        # Read the number of children.
        children = int(input("How many children? "))

        # Compute and display the amount of assistance.
        amount = compute_assistance(income, children)
        print("The assistance amount is $%.2f." % amount)

        # Read the next income value.
        income = float(input("What is the household income (-1 to quit)? "))


def compute_assistance(income, children):
    """
    Compute the amount of assistance provide by an NGO.

    :param income: the household annual income
    :param children: the number of children
    :return: the amount of financial assistance that will be provided
    """
    if 30000 < income <= 40000 and children >= 3:
        return 1000 * children
    if 20000 <= income <= 30000 and children >= 2:
        return 1500 * children
    if income < 20000:
        return 2000 * children
    return 0


# Call the main function.
if __name__== "__main__":
    main()

