#  Process a maze file, identifying all of the neighbors of each location.

# Open the maze file and read it.
def main():

    try:

        with open("maze.txt", "r", encoding='utf-8') as inf:
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
    for i in sorted(positions):
        print(i, ":", positions[i])

if __name__ == "__main__":

    main()
