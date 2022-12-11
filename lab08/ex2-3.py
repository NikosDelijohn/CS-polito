#!/usr/bin/python3

def take_turn(board, mark):
    """
    Process the turn for one player
    :param board: the game board to work with
    :param mark: the symbol used for the player
    """
    # Display the board.
    draw_board(board)

    # Read the user's move, ensuring that it is legal.
    print("Player %s, make your move: " % mark)
    row = int(input("  row: "))
    col = int(input("  col: "))
    while board[row][col] != " ":
        print("That wasn't a valid move, try again: ")
        row = int(input("  row: "))
        col = int(input("  col: "))

    # Update the board with the mark.
    board[row][col] = mark


def draw_board(board):
    """
    Draw the game board
    :param board: the game board to display
    """
    print("   0   1   2")
    for i in range(0, 2):
        print(f'{i}  {board[i][0]:<2}| {board[i][1]:<2}| {board[i][2]:<2}')
        print("  ---+---+---")
    print(f'{2}  {board[2][0]:<2}| {board[2][1]:<2}| {board[2][2]:<2}')


def game_won(board, mark):
    """
    Determine if a player has won the game
    :param board: the board to check for a winner
    :param mark: the mark to check for winning
    :return: True if the game was won with the given mark, False otherwise
    """
    # Check the rows and columns for a winner.
    for i in range(0, 3):
        if board[i][0] == mark and board[i][1] == mark and board[i][2] == mark:
            return True
        if board[0][i] == mark and board[1][i] == mark and board[2][i] == mark:
            return True
    # Check the diagonals for a winner.
    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True
    if board[2][0] == mark and board[1][1] == mark and board[0][2] == mark:
        return True
    return False


def is_full(board):
    """
    Determine if the board is full
    :param board: the board to check
    :return: True if the board is full, False otherwise
    """
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == " ":
                return False
    return True

def main():
    # Construct a new empty board.
    board = [[" "] * 3, [" "] * 3, [" "] * 3]

    # Keep making moves until a player has won.
    turn = "X"
    game_over = False
    while not game_over:
        if turn == "X":
            turn = "O"
        else:
            turn = "X"
        take_turn(board, turn)
        game_over = game_won(board, turn) or is_full(board)

    # Display the final game board and the winner.
    draw_board(board)
    if game_won(board, turn):
        print("Player", turn, "won!")
    else:  # is_full
        print("It was a tie.")

if __name__ == "__main__":
    main()