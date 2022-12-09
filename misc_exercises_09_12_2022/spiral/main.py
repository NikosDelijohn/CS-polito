from copy import deepcopy

N = int(input("Write N: "))

square = []
for i in range(N):
    square.append([])
    for j in range(N):
        square[i].append(0)
        

print(square)
count = 1
row = 0
col = 0
while row < N and col < N:
    for i in range(col, N):
        square[row][i] = count
        count += 1
    for i in range(row + 1, N):
        square[i][N - 1] = count
        count += 1
    for i in range(col + 2, N):
        square[N - 1][-i] = count
        count += 1
    for i in range(row + 1, N):
        square[-i][col] = count
        count += 1
    col += 1
    row += 1
    N -= 1

print(square)