# cli.py

from logic import TicTacToeGame

class TicTacToeCLI:
    def __init__(self, game):
        self.game = game

    def play(self):
        while not self.game.is_game_over():
            self.game.print_board()
            print(f"It's {self.game.get_current_player()}'s turn.")

            if self.game.is_single_player() and self.game.get_current_player() == self.game.get_bot_player():
                # If single player, let the bot make a move
                self.game.make_bot_move()
            else:
                # Input a move from the player
                try:
                    row = int(input("Enter the row (1, 2, or 3): ")) - 1  # Adjust to 0-based index
                    col = int(input("Enter the column (1, 2, or 3): ")) - 1  # Adjust to 0-based index
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue

                # Make a move
                if not self.game.make_move(row, col):
                    print("Invalid move. Try again.")
                    continue

            # Check if someone has won
            if self.game.get_winner():
                self.game.print_board()
                if self.game.get_winner() == "Tie":
                    print("It's a tie! The game is a draw.")
                else:
                    print(f"Player {self.game.get_winner()} wins!")

            # Switch to the other player's turn
            self.game.switch_player()


if __name__ == '__main__':
    # Initialize the game with the CLI
    game = TicTacToeGame()
    cli = TicTacToeCLI(game)
    cli.play()
