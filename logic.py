# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

def make_empty_board():
    return [
        ['', '', ''],
        ['', '', ''],
        ['', '', ''],
    ]

def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    for player in ['X', 'O']:
        # Check rows for a win
        for i in range(3):
            row_win = True
            for j in range(3):
                if board[i][j] != player:
                    row_win = False
                    break
            if row_win:
                return player

        # Check columns for a win
        for i in range(3):
            col_win = True
            for j in range(3):
                if board[j][i] != player:
                    col_win = False
                    break
            if col_win:
                return player

        # Check diagonal (top-left to bottom-right) for a win
        diagonal_win = True
        for i in range(3):
            if board[i][i] != player:
                diagonal_win = False
                break
        if diagonal_win:
            return player

        # Check diagonal (top-right to bottom-left) for a win
        diagonal_win = True
        for i in range(3):
            if board[i][2 - i] != player:
                diagonal_win = False
                break
        if diagonal_win:
            return player

    return None  # No winner yet


def other_player(player):
    """Given the character for a player, returns the other player."""
    return 'X' if player == 'O' else 'O'

def print_board(board):
    for row in board:
        print(row)

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False  # 如果有一个空格，游戏板未满
    return True  # 游戏板已满
