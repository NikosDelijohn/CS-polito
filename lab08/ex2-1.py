#!/usr/bin/python3

def neighbor_average(values, row, column):

    count = 0
    total = 0
    # iterate (i,j) over a 3x3 square, centered in (row, column)
    for i in range(row - 1, row + 2):  # alternative: for i in [row-1, row, row+1]:
        for j in range(column - 1, column + 2):
            # I must count the element if:
            # - it is not the "center" element itself
            # - it is not outside the table
            if (i, j) != (row, column) and 0 <= i < len(values) and 0 <= j < len(values[i]):
                total = total + values[i][j]
                count = count + 1

    return total / count

def main():
    # Setup a sample table.
    table = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]

    # Alternatively, setup a sample table using list comprehensions
    # w, h = 4, 4
    # table = [[y + 1 for x in range(w)] for y in range(h)]

    # print(table)
    for row in table:
        print('|'.join([f'{item:^5d}' for item in row]))  # create a temp list of string-formatted numbers

    # Demonstrate that neighbor_average works correctly.
    print("The average at (0,0) is", neighbor_average(table, 0, 0))
    print("The average at (1,2) is", neighbor_average(table, 1, 2))
    print("The average at (3,2) is", neighbor_average(table, 3, 2))

if __name__ == "__main__":

    main()