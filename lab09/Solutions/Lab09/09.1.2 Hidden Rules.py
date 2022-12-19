# Exercise 09.1.2
# Hidden Rules

# I.	1 2 3 4 5 6 7 8 9 10

l = []
for n in range(1, 11):
    l.append(n)
print(l)

# alternative
l = [n for n in range(1, 11)]
print(l)

# II.	0 2 4 6 8 10 12 14 16 18 20

l = []
for n in range(0, 11):
    l.append(2 * n)
print(l)

# alternative
l = [2 * n for n in range(0, 11)]
print(l)

# III.	1 4 9 16 25 36 49 64 81 100

l = []
for n in range(1, 11):
    l.append(n ** 2)
print(l)

# alternative
l = [n ** 2 for n in range(1, 11)]
print(l)

# IV.	0 0 0 0 0 0 0 0 0 0

l = []
for n in range(10):
    l.append(0)
print(l)

# alternative
l = [0 for _ in range(10)]
print(l)

# alternative
l = [0] * 10
print(l)

# V.	1 4 9 16 9 7 4 9 11

# is there a rule??? I don't think so...
l = [1, 4, 9, 16, 9, 7, 4, 9, 11]
print(l)

# VI.	0 1 0 1 0 1 0 1 0 1

l = []
for i in range(10):
    if i % 2 == 0:
        l.append(0)
    else:
        l.append(1)
print(l)

# alternative
l = [0, 1] * 5
print(l)

# alternative
l = [i % 2 for i in range(10)]
print(l)

# VII.	0 1 2 3 4 0 1 2 3 4

l = []
for n in range(0, 5):
    l.append(n)
for n in range(0, 5):
    l.append(n)
print(l)

# alternative
l = [0, 1, 2, 3, 4] * 2
print(l)

# alternative
l = [0, 1, 2, 3, 4]
l.extend(l)  # or l = l + l
print(l)

# alternative
l = [i % 5 for i in range(10)]
print(l)
