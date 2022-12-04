#  Simulate how parking slots fill up in a public parking.

# Define constants.
NUM_SLOTS = 11

def main():

    # Start with all slots unoccupied (free).
    occupied = []
    for i in range(NUM_SLOTS):
        occupied.append(False)

    # Loop as long as there is at least one unoccupied slot.
    while False in occupied:
        # Find the position and length of the longest sequence of unoccupied slots.
        longest_length = 0
        longest_pos = 0
        for i in range(len(occupied)):
            if not occupied[i]:
                current_length = 1
                pos = i + 1
                while pos < len(occupied) and not occupied[pos]:
                    current_length = current_length + 1
                    pos = pos + 1
                if current_length > longest_length:
                    longest_length = current_length
                    longest_pos = i

        # Fill in the middle position in the longest unoccupied run.
        occupied[longest_pos + longest_length // 2] = True

        # Display the current status of the parking.
        for i in range(0, len(occupied)):
            if occupied[i]:
                print("X ", end="")
            else:
                print("- ", end="")
        print()

if __name__ == "__main__":
    main()