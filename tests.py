# tests.py

import unittest
from logic import TicTacToe, HumanPlayer, BotPlayer

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        # Set up common objects for tests
        self.player1 = HumanPlayer("X", 1)
        self.player2 = HumanPlayer("O", 2)
        self.bot_player = BotPlayer("O", 2)

    def test_initialization(self):
        # Test the game initialization with an empty board
        game = TicTacToe(self.player1, self.player2)
        self.assertEqual(game.board, [[" "]*3 for _ in range(3)])
        self.assertEqual(game.player1, self.player1)
        self.assertEqual(game.player2, self.player2)
        self.assertEqual(game.current_player, self.player1)

    def test_switch_player(self):
        # Test switching between players
        game = TicTacToe(self.player1, self.player2)
        self.assertEqual(game.current_player, self.player1)
        game.switch_player()
        self.assertEqual(game.current_player, self.player2)
        game.switch_player()
        self.assertEqual(game.current_player, self.player1)

    def test_valid_move(self):
        # Test making a valid move
        game = TicTacToe(self.player1, self.player2)
        self.assertTrue(game.make_move((0, 0)))
        self.assertEqual(game.board[0][0], "X")

    def test_invalid_move(self):
        # Test making an invalid move
        game = TicTacToe(self.player1, self.player2)
        game.make_move((0, 0))
        self.assertFalse(game.make_move((0, 0)))  # Attempt to make a move in the same spot

    def test_winner_detection(self):
        # Test detecting a winner
        game = TicTacToe(self.player1, self.player2)
        game.make_move((0, 0))
        game.make_move((1, 0))
        game.make_move((0, 1))
        game.make_move((1, 1))
        game.make_move((0, 2))
        self.assertTrue(game.is_winner(self.player1))

    def test_draw_detection(self):
        # Test detecting a draw
        game = TicTacToe(self.player1, self.player2)
        game.make_move((0, 0))
        game.make_move((1, 0))
        game.make_move((2, 0))
        game.make_move((1, 1))
        game.make_move((0, 1))
        game.make_move((2, 1))
        game.make_move((1, 2))
        game.make_move((0, 2))
        game.make_move((2, 2))
        self.assertTrue(game.is_draw())

    def test_game_over_detection(self):
        # Test detecting game over (winner or draw)
        game = TicTacToe(self.player1, self.player2)
        game.make_move((0, 0))
        game.make_move((1, 0))
        game.make_move((0, 1))
        game.make_move((1, 1))
        game.make_move((0, 2))
        self.assertTrue(game.is_game_over())


if __name__ == "__main__":
    unittest.main()
