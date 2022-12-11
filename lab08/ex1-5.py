#!/usr/bin/python3
 
#!/usr/bin/python3

def merge(a : list , b : list ) -> list :

    retval = list()

    shortest_length = min(len(a),len(b))

    for index in range(shortest_length):
        retval.append(a[index])
        retval.append(b[index])

    for index in range(shortest_length, len(a)):

        retval.append(a[index])

    for index in range(shortest_length, len(b)):

        retval.append(b[index])

    return retval

def merge_with_slicing(a : list , b : list ) -> list:

    shortest_length = min(len(a),len(b))

    retval = [0] * shortest_length * 2

    retval[::2]  = a[:shortest_length]
    retval[1::2] = b[:shortest_length]

    retval.extend(a[shortest_length:]+b[shortest_length:])

    return retval


def main():

    test_list_a = [0, 2, 4, 6, 8, 10]
    test_list_b = [1, 3, 5, 7, 9, 11, 13]

    print(f"Merging {test_list_a} and {test_list_b} to {merge(test_list_a,test_list_b)}")

    test_list_c = [ 'R', 'N', 'M', 'I', 'E']
    test_list_d = [ 'I', 'O', ' ', 'A', 'D', 'N', '!', '!']

    print(f" <3 {merge(test_list_d,test_list_c)} <3")

if __name__ == "__main__": 
    main()