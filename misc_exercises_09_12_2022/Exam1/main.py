
'''
In "rules.txt" is defined a set of rules.

For each line:

- First, there is the date of start or end of the rule.
- Then, the name of the rule.
- Then, the charachter 'S' or 'E' meaning the rule 'S'tarted or 'E'nded.

A rule might not have an end, meaning it is currently active.

The entire file shall be coherent (a rule cannot end before it started).
If a rule is not coherent, then print an error message and invert start and end.

Given a date, the program shall print all the rules active in that date
(meaning: they started, but they did not finish yet)
'''
filename = "rules.txt"
rules = []

def find_rule(rule, list):
    result = []
    for r in list:
        if r[0] == rule:
            result = r
    return result


def compare_dates(first, second):
    result = 0
    first_date_as_tokens = first.split('/')
    second_date_as_tokens = second.split('/')
    if int(first_date_as_tokens[2]) > int(second_date_as_tokens[2]):
        result = 1
    elif int(first_date_as_tokens[2]) < int(second_date_as_tokens[2]):
        result = 2
    else:
        if int(first_date_as_tokens[1]) > int(second_date_as_tokens[1]):
            result = 1
        elif int(first_date_as_tokens[1]) < int(second_date_as_tokens[1]):
            result = 2
        else:
            if int(first_date_as_tokens[0]) > int(second_date_as_tokens[0]):
                result = 1
            elif int(first_date_as_tokens[0]) < int(second_date_as_tokens[0]):
                result = 2
    return result


def read_file():
    try:
        with open(filename) as f:
            for line in f.readlines():
                tokens = line.split('\n')[0].split('\r')[0].split(" ")
                date = tokens[0]
                rule_name = tokens[1]
                is_start_date = tokens[2] == 'S'
                rule = find_rule(rule_name, rules)
                if len(rule) == 0:
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
    read_file()
    date = '03/03/1994'
    for rule in rules:
        if compare_dates(date, rule[1]) <= 1:
            if compare_dates(rule[2], date) <= 1:
                print(rule[0])


if __name__ == '__main__':
    main()