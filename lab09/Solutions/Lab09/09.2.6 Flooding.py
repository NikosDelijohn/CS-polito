# Exercise 09.2.6
# Flooding

#  Read a height map and display which portions of it are covered in water
#  given a flood height.

# Define constant variables.
WIDTH = 10
HEIGHT = 410
NUM_LEVELS = 10


def main():
    heights = []

    # Read all the height values from the user.
    for i in range(0, HEIGHT):
        heights.append([])
        for j in range(0, WIDTH):
            level = float(input(f"Enter the value for row {i} column {j}: "))
            heights[i].append(level)

    # Compute minimum and maximum heights
    min_h = 1000000
    max_h = 0
    for row in heights:
        min_row = min(row)  # min of the whole row
        max_row = max(row)  # max of the whole row
        if min_row < min_h:
            min_h = min_row
        if max_row > max_h:
            max_h = max_row

    # Display the map for 10 different flood levels.
    for step in range(0, NUM_LEVELS + 1):
        # the range from min to max is divided in NUM_LEVELS equal steps
        level = min_h + (step / NUM_LEVELS) * (max_h - min_h)
        print(f"Water level: {level:.2f}")
        flood_map(heights, level)
        print()


def flood_map(heights, water_level):
    """
    Draw a flood map for a certain water level.

    :param heights:  a table of terrain heights
    :param water_level: a flood level for the terrain
    """
    for i in range(0, HEIGHT):
        for j in range(0, WIDTH):
            if heights[i][j] <= water_level:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


# Call the main function.
main()
