# Create a NxN spiral of integer numbers
from pprint import pprint

def main():
    n = int(input('Size of the spiral: '))

    # build a nxn matrix, filled with 0
    matrix = []
    for row in range(n):
        matrix.append([0] * n)

    # the spiral can be seen as a sequence of "rings".
    # - if N is even, we have N/2 rings
    # - if N is odd, we have N/2 rings, plus a "central" value
    # ring=0 -> the external ring

    start = 1
    for ring in range(n // 2):
        start = build_ring(matrix, ring, start)
    if n % 2 == 1:
        matrix[n // 2][n // 2] = start

    pprint(matrix)


def build_ring(mat, ring, start):
    n = len(mat)
    # the ring starts at cell mat[ring][ring]
    # go right from [ring][ring]->[ring][n-1-ring]
    for col in range(ring, n - ring):
        mat[ring][col] = start
        start = start + 1
    # go down, on the same column [ring+1][n-1-ring]->[n-1-ring][n-1-ring]
    for row in range(ring + 1, n - ring):
        mat[row][n - ring - 1] = start
        start = start + 1
    # go left, on the same row [n-1-ring][n-1-ring-1]->[n-1-ring][ring]
    for col in range(n - ring - 2, ring - 1, -1):
        mat[n - ring - 1][col] = start
        start = start + 1
    # go up, on the same column [n-1-ring-1][ring] -> [ring+1][ring]
    for row in range(n - ring - 2, ring, -1):
        mat[row][ring] = start
        start = start + 1

    return start

if __name__ == "__main__":

    main()
