# Exercise 3.1
print("Welcome to CS labs!")

# Exercise 3.2
sum = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
print(sum)

# Exercise 3.3
mul = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10
print(mul)

# Exercise 3.4 
print(
    "   AAA     SSSSS   CCCCC  IIII IIII\n"
    "  AA AA   SS   SS CC   CC  II   II \n"
    " AA   AA  SS      CC       II   II \n"
    "AA     AA  SSSSS  CC       II   II \n"
    "AAAAAAAAA      SS CC       II   II \n"
    "AA     AA SS   SS CC   CC  II   II \n"
    "AA     AA  SSSSS  CCCCCC  IIII IIII\n"
)

# Exercise 3.5
print("G\n"
"A\n"
"B\n"
"R\n"
"I\n"
"E\n"
"L\n"
"E\n")

# Exercise 3.6
def interest(interest_rate, balance):
    increase = interest_rate * balance / 100
    return balance + increase

balance = 1000
for year in range(1, 3 + 1):
    balance = interest(5, balance)
    print("Year " + str(year) + " balance: " + str(balance))

# Exercise 3.7
print(
    "+----------+\n"
    "|Gabrielele|\n"
    "+----------+\n"
)

# Exercise 3.9
print("abcd" + "01234" + "abcd" + "01234")

# Exercise 3.10
for row in range(0, 5):
    if row % 2 == 0:
        print("01010")
    else:
        print("10101")

# Exercise 3.11
print(100*"-")

# Exercise 3.12 
print(100*"0")

# Exercise 3.13
def fibonacci(sequence):
    return sequence + [sequence[-2] + sequence[-1]]

sequence = [0, 1]
for i in range(2, 4):
   sequence = fibonacci(sequence)

print(sequence[-1]) 

# Exercise 3.14
for i in range(0, len(sequence)):
    print(sequence[i])

# Exercise 3.15
def percentage_complete(completed, total):
    return 100 * completed / total

print(
    "+--------------------------------------------------------+\n"
    f"|I've finished this session with a percentage of: {percentage_complete(15, 15):.2f}%|\n"
    "+--------------------------------------------------------+")
