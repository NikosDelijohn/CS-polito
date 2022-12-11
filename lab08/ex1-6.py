#!/usr/bin/python3 

def merge_sorted(a : list, b : list) -> list:

    a_pos = 0
    b_pos = 0
    result = []

    # As long as there is an unprocessed element in either list.
    while a_pos < len(a) or b_pos < len(b):
        # If there are elements in both lists then take an element from the
        # list that starts with the smaller element.
        if a_pos < len(a) and b_pos < len(b):
            if a[a_pos] <= b[b_pos]:
                result.append(a[a_pos])
                a_pos = a_pos + 1
            else:
                result.append(b[b_pos])
                b_pos = b_pos + 1
        # If only list 'a' has elements then process its first element.
        elif a_pos < len(a):
            result.append(a[a_pos])
            a_pos = a_pos + 1
        # If only list 'b' has elements then process its first element.
        else:
            result.append(b[b_pos])
            b_pos = b_pos + 1

    return result

def main():
    # Set up two sample lists.
    a = [1, 4, 9, 16]
    b = [4, 7, 9, 9, 11, 19]

    # Demonstrate that merge_sorted works correctly.
    print("List a is", a)
    print("List b is", b)
    merged = merge_sorted(a, b)
    print("The merged list is", merged)

    print("In reverse order, the result should be the same:")
    merged = merge_sorted(b, a)
    print("The merged list is", merged)


# Call the main function.
if __name__ == "__main__":
    main()