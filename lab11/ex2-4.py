#  Compute the escape path from a maze.

PATH_TO_FILE = "input_files/ex2-3/maze.txt"

# Open the maze file and read it.
def main():

    try:

        with open(PATH_TO_FILE, "r", encoding="utf-8") as inf:
            maze = []
            for line in inf:
                maze.append(line.rstrip())
    except FileNotFoundError:
        exit(f"Tried to open file maze.txt. It's not found!")


    # Create the dictionary.
    positions = {}
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == " ":
                positions[(row, col)] = set()
                # Check left.
                if row > 0 and maze[row - 1][col] == " ":
                    positions[(row, col)].add((row - 1, col))
                # Check right.
                if row < len(maze) - 1 and maze[row + 1][col] == " ":
                    positions[(row, col)].add((row + 1, col))
                # Check up.
                if col > 0 and maze[row][col - 1] == " ":
                    positions[(row, col)].add((row, col - 1))
                # Check down.
                if col < len(maze[row]) - 1 and maze[row][col + 1] == " ":
                    positions[(row, col)].add((row, col + 1))

    # Print the dictionary.
    # for i in sorted(positions):
    #     print(i, ":", positions[i])

    # Create the escape dictionary.
    escape = {}
    for key in positions:
        escape[key] = "?"

    # Traverse the dictionary, replacing boundary entries with the escape direction.
    for (r, c) in escape:
        if r == 0:
            escape[(r, c)] = "N"
        if r == len(maze) - 1:
            escape[(r, c)] = "S"
        if c == 0:
            escape[(r, c)] = "W"
        if c == len(maze[r]):
            escape[(r, c)] = "E"

    # Repeatedly traverse the keys until no changes are made.
    changed = True
    while changed:
        changed = False
        for (r, c) in escape:
            if escape[(r, c)] == "?":
                for (er, ec) in positions[(r, c)]:
                    if escape[(er, ec)] != "?":
                        if er < r:
                            escape[(r, c)] = "N"
                        elif er > r:
                            escape[(r, c)] = "S"
                        elif ec < c:
                            escape[(r, c)] = "W"
                        else:
                            escape[(r, c)] = "E"
                        changed = True

    # Update the maze with the escape directions.
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == " ":
                maze[row] = maze[row][:col] + escape[(row, col)] + maze[row][col + 1:]

    # Display the maze.
    for row in maze:
        print(row)

if __name__ == "__main__":

    main()
