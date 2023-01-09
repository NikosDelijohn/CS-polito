#  Compute the sum of two sparse arrays stored in dictionaries.

def main():
    a = {5: 4, 9: 2, 10: 9}
    b = {5: 4, 8: 4, 10: 4}

    print("a is", a)
    print("b is", b)
    print("The sum of a and b is:", sparse_array_sum(a, b))


def sparse_array_sum(a, b):
    """
    Compute the sum of two sparse arrays

    :param a: the first array to include in the sum
    :param b: the second array to include in the sum
    :return: a new dict representing the sum array
    """
    retval = dict(a)  # make a copy of 'a' to become the result
    for key in b:
        if key in retval:
            retval[key] = retval[key] + b[key]
        else:
            retval[key] = b[key]
    return retval


# Call the main function.
if __name__ == "__main__":

    main()