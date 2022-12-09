table = []
N = 4

def create_table():
    count = 0
    for i in range(N):
        row = []
        for j in range(N):
            row.append(count)
            count += 1
        table.append(row)

# 0 1 2 3
# 4 5 6 7
# 8 9 10 11
# 12 13 14 15
#
def neighbour_average(values, row, column) -> float:
    sum = 0
    count = 0
    if column > 0:
        sum += values[row][column - 1]
        count += 1
    if column < len(values[row]) - 1:
        sum += values[row][column + 1]
        count += 1
    if row > 0:
        sum += values[row - 1][column]
        count += 1
    if row < len(table) - 1:
        sum += values[row + 1][column]
        count += 1
    if row > 0 and column > 0:
        sum += values[row - 1][column - 1]
        count += 1
    if row > 0 and column < len(values[row]) - 1:
        sum += values[row - 1][column + 1]
        count += 1
    if row < len(values) - 1 and column > 0:
        sum += values[row + 1][column - 1]
        count += 1
    if row < len(values) -1 and column < len(values[row]) - 1:
        sum += values[row + 1][column + 1]
        count += 1
    return sum / count

def main():
    create_table()
    avg = neighbour_average(table, 0, 1)
    print(table)
    print(avg)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
