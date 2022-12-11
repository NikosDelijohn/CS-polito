#!/usr/bin/python3
#!/usr/bin/python3

def fill_matrix_from_user():

    retval = list()

    for row in range(4):

        current_row = list()

        for col in range(4):

            user_input = input(f"Enter a number for cell {row} {col} : ")

            while not user_input.isnumeric():
                user_input = input(f"Enter a number for cell {row} {col} : ")

            current_row.append(int(user_input))

        retval.append(current_row)

    return retval

def print_matrix(matrix):

    for row in matrix:

        list_to_string = "|".join( [f'{number:^3}' for number in row] )
        print(list_to_string)

def is_magic_square(matrix):

    magic_sum = sum(matrix[0])

    # [1] Are all the numbers from 1..16 present ?

    for number in range(1,17):
        if \
        (
        number not in matrix[0] and
        number not in matrix[1] and
        number not in matrix[2] and
        number not in matrix[3]
        ):
            return False

    # [2.a] Checking the sum of each row (excluding 0)
    for row in range(1,4):

        if sum(matrix[row]) != magic_sum:
            return False

    # [2.b] Checking the sum of each col
    for col in range(4):

        if matrix[0][col] + matrix[1][col] + matrix[2][col] + matrix[3][col] != magic_sum:
            return False

    # [2.c] Checking the sum of each diagonal

    if matrix[0][0] + matrix[1][1] + matrix[2][2] + matrix[3][3] != magic_sum:

        return False

    if matrix[0][3] + matrix[1][2] + matrix[2][1] + matrix[3][0] != magic_sum:

        return False

    return True


def main():

    matrix = fill_matrix_from_user()

    print_matrix(matrix)

    print(f""" *DRUM ROLL*
It {'is' if is_magic_square(matrix) else "isn't" } a magic square!""")


if __name__ == "__main__":

    main()
