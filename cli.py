# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, get_winner, print_board, is_board_full, other_player


# Reminder to check all the tests


if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    current_player = "X"
    while winner is None:
        print_board(board)
        print(f"It's {current_player}'s turn.")

        # Input a move from the player
        try:
            row = int(input("Enter the row (1, 2, or 3): ")) - 1  # Adjust to 0-based index
            col = int(input("Enter the column (1, 2, or 3): ")) - 1  # Adjust to 0-based index
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Check if the move is valid
        if row not in (0, 1, 2) or col not in (0, 1, 2) or board[row][col] != '':
            print("Invalid move. Try again.")
            continue

        # Update the board
        board[row][col] = current_player

        # Check if someone has won
        winner = get_winner(board)
        if winner:
            print_board(board)
            if winner == "Tie":
                print("It's a tie! The game is a draw.")
            else:
                print(f"Player {winner} wins!")
        else:
            # Switch to the other player's turn
            current_player = 'O' if current_player == 'X' else 'X'
