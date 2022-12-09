rules = []

FILENAME = "rules.txt"

def date_into_numbers(date: str) -> (int, int, int):
    tokens = date.split("/")
    return int(tokens[2]), int(tokens[1]), int(tokens[0])

def find_rule(name: str) -> [str, str, str]:
    for rule in rules:
        if rule[0] == name:
            return rule

# -1 = even
# 0 = first date is greater
# 1 = second date is greater
def compare_dates(date1: str, date2: str) -> int:
    d1 = date_into_numbers(date1)
    d2 = date_into_numbers(date2)
    result = -1
    if d1[0] > d2[0]:
        result = 0
    elif d1[0] < d2[0]:
        result = 1
    else:
        if d1[1] > d2[1]:
            result = 0
        elif d1[1] < d2[1]:
            result = 1
        else:
            if d1[2] > d2[2]:
                result = 0
            elif d1[2] < d2[2]:
                result = 1
    return result

def rule_active(date: str, rule: list) -> bool:
    if compare_dates(rule[1], date) == 1:
        if len(rule[2]) == 0 or compare_dates(rule[2], date) == 0:
            return True
    return False

def read_dates(filename: str):
    with open(filename) as f:
        try:
            for line in f.readlines():
                tokens = line.split('\n')[0].split('\r')[0].split(" ")
                date = tokens[0]
                rule_name = tokens[1]
                is_start_date = tokens[2] == 'S'
                rule = find_rule(rule_name)
                if rule is None:
                    rule = [
                        rule_name,
                        "",
                        ""
                    ]
                    rules.append(rule)
                if is_start_date:
                    rule[1] = date
                else:
                    rule[2] = date
                if len(rule[1]) > 0 and len(rule[2]) > 0:
                    if compare_dates(rule[1], rule[2]) == 0:
                        temp = rule[1]
                        rule[1] = rule[2]
                        rule[2] = temp
                        print(f"WARNING!: rule {rule_name} has inverted start and end. We fixed this!")
        except FileNotFoundError:
            print(f"File not found: {filename}")
            return -1

def main():
    read_dates(FILENAME)
    print(rules)
    date_ok = False
    date = ""
    while not date_ok:
        date = input("Write a date: ")
        if len(date.split("/")) == 3:
            date_ok = True
    print("Showing active rules:")
    for rule in rules:
        if rule_active(date, rule):
            print(rule)


if __name__ == '__main__':
    main()
