# cli.py

from logic import TicTacToe, HumanPlayer, BotPlayer

def play_game():
    global games_played
    total_games = 100
    games_played = 0

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

    while games_played < total_games:
        print("\nNew Game:")
        
        # Record the first move of player1 at the beginning of each game
        # game.record_first_move_per_game()

        while not game.is_game_over():
            if game.current_player == player1:
                move_result = game.current_player.make_move(game)
            else:
                move_result = game.current_player.make_move(game)

        print(game.get_game_result())

        # Check if move_result is a tuple before recording winner
        if game.is_winner(player1):
            game.record_winner(player1)
        elif game.is_winner(player2):
            game.record_winner(player2)
        else:
            game.record_winner(None)

        games_played += 1
        print(f"\nGame {games_played} completed out of {total_games}.\n")

        game.reset_game()

    print("\nAll games completed.")

if __name__ == "__main__":
    play_game()
