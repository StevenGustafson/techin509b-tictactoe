# cli.py

from logic import TicTacToe, HumanPlayer, BotPlayer

def play_game():
    def print_board(board):
        for i in range(3):
            for j in range(3):
                print(f" {board[i][j]} ", end="")
                if j < 2:
                    print("|", end="")
            print("\n", end="")
            if i < 2:
                print("-----------")
        print("\n")

    player_count = int(input("Enter the number of players (1 or 2): "))
    if player_count == 1:
        player1 = HumanPlayer("X", 1)
        player2 = BotPlayer("O", 2)
    elif player_count == 2:
        player1 = HumanPlayer("X", 1)
        player2 = HumanPlayer("O", 2)
    else:
        print("Invalid number of players. Exiting.")
        return

    game = TicTacToe(player1, player2)

    total_games = 1000
    games_played = 0

    while games_played < total_games:
        print("\nNew Game:")
        while not game.is_game_over():
            # print_board(game.board)
            move_result = game.current_player.make_move(game)
            # if move_result:
                # print(move_result)

        # print_board(game.board)
        print(game.get_game_result())

        # Log winner data
        if game.is_winner(game.player1):
            game.record_winner(game.player1)
        elif game.is_winner(game.player2):
            game.record_winner(game.player2)
        else:
            game.record_winner(None)  # Log draw

        games_played += 1
        print(f"\nGame {games_played} completed out of {total_games}.\n")

        # Reset the game for the next iteration
        game.reset_game()

    print("\nAll games completed.")

if __name__ == "__main__":
    play_game()
