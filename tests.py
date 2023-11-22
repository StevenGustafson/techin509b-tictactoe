# tests.py

import unittest
from logic import TicTacToeGame

class TestTicTacToeGame(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToeGame()

    def test_initialization_empty_board(self):
        # Test that the game is initialized with an empty board
        empty_board = [
            ['', '', ''],
            ['', '', ''],
            ['', '', ''],
        ]
        self.assertEqual(self.game.board, empty_board)

    def test_single_player_initialization(self):
        # Test that the game is initialized with 1 player (human-bot)
        self.game = TicTacToeGame(single_player=True)
        self.assertTrue(self.game.is_single_player())
        self.assertIsNotNone(self.game.get_bot_player())

    def test_two_players_initialization(self):
        # Test that the game is initialized with 2 players (human-human)
        self.game = TicTacToeGame(single_player=False)
        self.assertFalse(self.game.is_single_player())
        self.assertIsNone(self.game.get_bot_player())

    def test_players_assigned_unique_pieces(self):
        # Test that players are assigned unique pieces (X or O)
        player1 = self.game.get_current_player()
        self.game.switch_player()
        player2 = self.game.get_current_player()
        self.assertNotEqual(player1, player2)

    def test_players_take_turns(self):
        # Test that after one player plays, the other player has a turn
        initial_player = self.game.get_current_player()
        self.game.switch_player()
        next_player = self.game.get_current_player()
        self.assertNotEqual(initial_player, next_player)

    def test_valid_moves(self):
        # Test that players can play only in viable spots
        self.assertTrue(self.game.make_move(0, 0))
        self.assertFalse(self.game.make_move(0, 0))  # Duplicate move should fail
        self.assertFalse(self.game.make_move(3, 3))  # Out of bounds move should fail

    def test_game_winner_detection(self):
        # Test that all winning end of the games are detected
        winning_combinations = [
            [(0, 0), (0, 1), (0, 2)],  # Top row
            [(1, 0), (1, 1), (1, 2)],  # Middle row
            [(2, 0), (2, 1), (2, 2)],  # Bottom row
            [(0, 0), (1, 0), (2, 0)],  # Left column
            [(0, 1), (1, 1), (2, 1)],  # Middle column
            [(0, 2), (1, 2), (2, 2)],  # Right column
            [(0, 0), (1, 1), (2, 2)],  # Diagonal top-left to bottom-right
            [(0, 2), (1, 1), (2, 0)],  # Diagonal top-right to bottom-left
        ]

        for combination in winning_combinations:
            self.game = TicTacToeGame()
            for move in combination:
                self.assertTrue(self.game.make_move(*move))
                self.game.switch_player()
            self.assertEqual(self.game.get_winner(), self.game.other_player(self.game.get_current_player()))

    def test_draw_game_detection(self):
        # Test that draw games are identified
        draw_board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O'],
        ]
        self.game.board = draw_board
        self.assertTrue(self.game.is_board_full())
        self.assertIsNone(self.game.get_winner())
        self.assertTrue(self.game.is_game_over())


if __name__ == '__main__':
    unittest.main()

