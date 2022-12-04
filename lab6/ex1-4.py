
"""
Compute the future value of an investment.
"""
def main():
    print(f"In 3 years at 4%, $10000 will be ${future_value(10000, 4, 3):.2f}")
    print(f"In 4 years at 3.5%, $5000 will be ${future_value(5000, 3.5, 4):.2f}")
    print(f"In 1 year at 10%, $1000 will be ${future_value(1000, 10, 1):.2f}")


def future_value(init, rate, years):
    """
    Compute the future value of an investment.

    :param init: the initial value of the investment
    :param rate: the interest rate in percent
    :param years: the number of years
    :return: the future value of the investment
    """
    return init * (1 + rate / 100) ** years

if __name__ == "__main__":
    main()