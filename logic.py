# logic.py

import random

class TicTacToeGame:
    def __init__(self):
        self.board = self.make_empty_board()
        self.winner = None
        self.current_player = "X"
        self.single_player = None
        self.bot_player = None

    def make_empty_board(self):
        return [
            ['', '', ''],
            ['', '', ''],
            ['', '', ''],
        ]

    def get_winner(self):
        # Implementation remains the same

    def other_player(self, player):
        return 'X' if player == 'O' else 'O'

    def print_board(self):
        for row in self.board:
            print(row)

    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def is_single_player(self):
        return self.single_player

    def get_bot_player(self):
        return self.bot_player

    def is_game_over(self):
        return self.winner is not None or self.is_board_full()

    def get_current_player(self):
        return self.current_player

    def make_move(self, row, col):
        if row not in (0, 1, 2) or col not in (0, 1, 2) or self.board[row][col] != '':
            return False
        self.board[row][col] = self.current_player
        self.check_winner()
        return True

    def make_bot_move(self):
        # Simplified random move for the bot
        available_moves = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == '']
        if available_moves:
            row, col = random.choice(available_moves)
            self.board[row][col] = self.current_player
            self.check_winner()

    def switch_player(self):
        self.current_player = self.other_player(self.current_player)

    def check_winner(self):
        for player in ['X', 'O']:
            # Implementation remains the same
            # ...

# Add relevant methods and properties to support single player and bot functionality
