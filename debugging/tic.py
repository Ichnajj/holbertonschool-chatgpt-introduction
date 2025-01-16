#!/usr/bin/python3

def print_board(board):
    """Prints the game board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Checks if a player has won the game."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """Runs the main game loop for Tic-Tac-Toe."""
    board = [[" "]*3 for _ in range(3)]  # Initialize empty board
    player = "X"  # Player X starts

    while not check_winner(board):
        print_board(board)
        
        # Get user input with validation
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))

            # Validate input range
            if row not in range(3) or col not in range(3):
                print("Invalid input! Row and column must be between 0 and 2. Try again.")
                continue

            if board[row][col] == " ":
                board[row][col] = player
                # Switch player
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")

        except ValueError:
            print("Invalid input! Please enter integers only. Try again.")

    print_board(board)
    # The winner is the player who made the last successful move, so we need to switch the player before announcing the winner
    winner = "O" if player == "X" else "X"
    print("Player " + winner + " wins!")

tic_tac_toe()
