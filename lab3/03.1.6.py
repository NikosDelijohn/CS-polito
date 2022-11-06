# Exercise 03.1.6
# De Morgan

x = int(input("Insert an integer number: "))
print()

# Case I
expr1 = not (x > 0 and x < 100)
expr2 = x <= 0 or x >= 100
print('not (x > 0 and x < 100)', expr1)
print('x <= 0 or x >= 100', expr2)
print()

# Case II
expr1 = not (x > 0 or x < 100)
expr2 = x <= 0 and x >= 100
print('not (x > 0 or x < 100)', expr1)
print('x <= 0 and x >= 100', expr2)
print()

# Case III
expr1 = not (x > 0 or 100 < x)
expr2 = x <= 0 and 100 >= x
print('not (x > 0 or 100 < x)', expr1)
print('x <= 0 and 100 >= x', expr2)
print()

# Case IV
expr1 = not (x > 0 and x < 100 or x == -1)
# De Morgan's law requires 2 steps, first apply the 'or'
# not(x > 0 and x < 100) and x != -1
# and then appy the parenthesized 'and'
# (x <=0 or x >=100) and x != -1
# attention, do not remove the parenthesis, since 'and' has precedence over 'or'
expr2 = (x <= 0 or x >= 100) and x != -1
print('not (x > 0 and x < 100 or x == -1)', expr1)
print('(x <= 0 or x >= 100) and x != -1', expr2)
