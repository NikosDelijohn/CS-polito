#!/usr/bin/python3

def get_table_dimensions() -> tuple:

    M = input("> Rows: ")
    while not M.isnumeric():
        M = input("> Rows: ")
    
    N = input("> Columns: ")
    while not N.isnumeric():
        N = input("> Columns: ")

    return (int(M),int(N))

def print_table(table : list) -> None:

    cell_width = len(max([str(x) for row in table for x in row]))

    rows = len(table)
    cols = len(table[0])

    print(f"+{ ('-'*(cell_width+2) + '+' ) * cols}")
    
    for row in table: 
        
        print('|', end='')

        for index,element in enumerate(row): 

            print(f" {element:^} |",end = '')

        print(f"\n+{ ('-'*(cell_width+2) + '+' ) * cols}")

def main():
     
    rows, cols = get_table_dimensions()

    # 1. Initialize the table with zeroes
    table = [[0 for col in range(cols)] for row in range(rows)] 
    print_table(table)

    # 2. Replace all elements with 1 
    for row in range(len(table)):

        for col in range(len(table)): 

            table[row][col] = 1 

    print_table(table)

    # 3. Zero-One pattern 
    for row in range(len(table)):

        for col in range(len(table)):

            table[row][col] = 0 if (row+col) % 2 == 0 else 1

    print_table(table)

    # 4. Zeroes on top and bot row
    for col in range(len(table[0])): 
        table[0][col] = 0
        table[-1][col] = 0

    print_table(table)
    
    # 5. Ones in first and last col
    for row in range(len(table)):

        table[row][0] = 1
        table[row][-1] = 1
    
    print_table(table)

    # 6. Sum of all elements
    print(f"Sum of all elements is: {sum([x for row in table for x in row])}")

if __name__ == "__main__":
    main()