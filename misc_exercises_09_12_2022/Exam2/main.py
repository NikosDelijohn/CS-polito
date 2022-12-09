
def print_hi(name):
    numbers = [1, 6, 13243, 45]
    for number in numbers:
        num_str = str(number)
        N = len(num_str)
        part_result = 0
        for digit in num_str:
            power = int(digit) ** N
            part_result += power
        print(number)
        print(part_result)
        print(number == part_result)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
