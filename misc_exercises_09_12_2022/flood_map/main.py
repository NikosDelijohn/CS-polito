def create_table(N):
    count = 0.0
    result = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(count)
            count += 0.1
        result.append(row)
    return result

def create_map(N):
    result = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(' ')
        result.append(row)
    return result

def flood_map(heights, water_level):
    result = create_map(len(heights))
    for x in range(len(heights)):
        for y in range(len(heights[x])):
            if water_level >= heights[x][y]:
                result[x][y] = '*'
            else:
                result[x][y] = '_'
    return result


def main():
    table = create_table(10)
    print(table)
    res = flood_map(table, 1.2)
    for x in range(len(res)):
        for y in range(len(res[x])):
            print(res[x][y], end='')
        print("")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
