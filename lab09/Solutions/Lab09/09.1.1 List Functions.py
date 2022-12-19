# Exercise 09.1.1
# List functions

#  Implement and demonstrate a collection of list functions.

# Define constant variables.
ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# alternative: ONE_TEN = list(range(1, 11))


def main():
    print("The original data for all functions is: ", ONE_TEN)

    # Demonstrate swapping the first and last element.
    data = list(ONE_TEN)
    swap_first_last(data)
    print("After swapping first and last: ", data)

    # Demonstrate shifting to the right.
    data = list(ONE_TEN)
    shift_right(data)
    print("After shifting right: ", data)

    # Demonstrate replacing even elements with zero.
    data = list(ONE_TEN)
    replace_even(data)
    print("After replacing even elements: ", data)

    # Demonstrate replacing values with the larger of their neighbors.
    data = list(ONE_TEN)
    replace_neighbors(data)
    print("After replacing with neighbors: ", data)

    # Demonstrate removing the middle element.
    data = list(ONE_TEN)
    remove_middle(data)
    print("After removing the middle element(s): ", data)

    # Demonstrate moving even elements to the front of the list.
    data = list(ONE_TEN)
    even_to_front(data)
    print("After moving even elements: ", data)

    # Demonstrate finding the second largest value.
    print("The second largest value is: ", second_largest(ONE_TEN))

    # Demonstrate testing if the list is in increasing order.
    print("The list is in increasing order: ", is_increasing(ONE_TEN))

    # Demonstrate testing if the list contains adjacent duplicates.
    print("The list has adjacent duplicates: ", has_adjacent_duplicate(ONE_TEN))

    # Demonstrate testing if the list contains duplicates.
    print("The list has duplicates: ", has_duplicate(ONE_TEN))


def swap_first_last(data):
    """
    Swap the first and last element in a list

    :param data: the list of values to process
    """
    if len(data) == 0:
        return

    temp = data[0]
    data[0] = data[len(data) - 1]
    data[len(data) - 1] = temp

    # alternative: data[0], data[-1] = data[-1], data[0]


def shift_right(data):
    """
    Shift the elements to the right

    :param data: the list of values to process
    """
    if len(data) == 0:
        return

    last = data[len(data) - 1]
    for i in range(len(data) - 1, 0, -1):
        # Iteration starting from the last element in the list and ending at the second one (i = 1)
        data[i] = data[i - 1]
    data[0] = last

    # Shortcut using slices and tuples
    # (data[0], data[1:]) = (data[-1], data[:-1])

    # Alternate solution with pop and insert methods
    # last = data.pop(len(data) - 1)
    # data.insert(0, last)


def replace_even(data):
    """
    Replace all even elements in the list with 0.

    :param data: the list of values to process
    """
    for i in range(0, len(data)):
        if data[i] % 2 == 0:
            data[i] = 0


def replace_neighbors(data):
    """
    Replace each value with the larger of its neighbors

    :param data: the list of values to process
    """
    old_values = list(data)
    for i in range(1, len(data) - 1):
        data[i] = max(old_values[i - 1], old_values[i + 1])


def remove_middle(data):
    """
    Remove the middle element or elements from a list

    :param data: the list of values to process
    """
    if len(data) == 0:
        return

    if len(data) % 2 == 1:
        data.pop(len(data) // 2)
    else:
        data.pop(len(data) // 2)
        data.pop(len(data) // 2)


def even_to_front(data):
    """
    Move even elements to the front of the list

    :param data: the list of values to process
    """
    even_pos = 0
    pos = 0
    while pos < len(data):
        if data[pos] % 2 == 0:
            temp = data.pop(pos)
            data.insert(even_pos, temp)
            even_pos = even_pos + 1
        pos = pos + 1


def second_largest(data):
    """
    Identify the second largest value in a list

    :param data: the list of values to process
    :return: the second largest value in the list
    """
    largest = max(data)
    second_largest_value = min(data)
    for value in data:
        if value > second_largest_value and value != largest:
            second_largest_value = value
    return second_largest_value
    # WARNING: does not work if the 1st and 2nd largest are equal

    # alternative
    # data.sort(reverse=True)
    # second_large = data[1]


def is_increasing(data):
    """
    Determine whether or not the list is in increasing order

    :param data: the list of values to process
    :return: True if the list is in increasing order, False otherwise
    """
    for i in range(0, len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True


def has_adjacent_duplicate(data):
    """
    Determine if the list contains adjacent duplicate elements

    :param data: the list of values to process
    :return: True if the list contains adjacent duplicates, False otherwise
    """
    for i in range(0, len(data) - 1):
        if data[i] == data[i + 1]:
            return True
    return False


def has_duplicate(data):
    """
    Determine if the list contains duplicate elements
    :param data: the list of values to process
    :return: True if the list contains duplicates, False otherwise
    """
    for i in range(0, len(data) - 1):
        for j in range(i + 1, len(data)): # avoid comparing data[i] with itself!!
            if data[i] == data[j]:
                return True
    return False


# Call the main function.
main()
