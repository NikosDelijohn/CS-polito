# Exercise 03.1.1
# True or False

from math import sqrt

# Comparison I
if 1 == 1:
    print("1 == 1? True")
else:
    print("1 == 1? False")

# Comparison II
if 1 == 1.0:
    print("1 == 1.0? True")
else:
    print("1 == 1.0? False")

# Comparison III
if 2.0 == sqrt(4.0):
    print("2.0 == sqrt(4.0)? True")
else:
    print("2.0 == sqrt(4.0)? False")

# Comparison IV
if '1' == 1:
    print("'1' == 1? True")
else:
    print("'1' == 1? False")

# Comparison V
if 'ciao' == 'Ciao':
    print("'ciao' == 'Ciao'? True")
else:
    print("'ciao' == 'Ciao'? False")



# ALTERNATE SOLUTION: the result of a comparison (e.g. 1==1) is itslef a boolean value,
# and can be memorized in a variable. Said variable can be either True or False
# (predefined constants in Python) and, as such, can be printed

comparison_I = (1 == 1)
print("1 == 1?", comparison_I)

comparison_II = (1 == 1.0)
print("1 == 1.0?", comparison_II)

comparison_III = (2.0 == sqrt(4.0))
print("2.0 == sqrt(4.0)?", comparison_III)

comparison_IV = ('1' == 1)
print("'1' == 1?", comparison_IV)

comparison_V = ('ciao' == 'Ciao')
print("'ciao' == 'Ciao'?", comparison_V)
