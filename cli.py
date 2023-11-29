# cli.py

from logic import TicTacToe, HumanPlayer, BotPlayer

def play_game():
    player_count = int(input("Enter the number of players (1 or 2): "))
    if player_count == 1:
        player1 = HumanPlayer("X",  1)  # Provide a value for the 'number' parameter
        player2 = BotPlayer("O",  2)    # Provide a value for the 'number' parameter
    elif player_count == 2:
        player1 = HumanPlayer("X", 1)  # Provide a value for the 'number' parameter
        player2 = HumanPlayer("O",  2)  # Provide a value for the 'number' parameter
    else:
        print("Invalid number of players. Exiting.")
        return

    game = TicTacToe(player1, player2)

    while True:
        print("\nNew Game:")
        while not game.is_game_over():
            print_board(game.board)
            move_result = game.current_player.make_move(game)
            if move_result:
                print(move_result)

        print_board(game.board)
        print(game.get_game_result())
        if not play_again():
            break
        else:
            game.reset_game()

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

def play_again():
    return input("Do you want to play again? (yes/no): ").lower().startswith('y')

if __name__ == "__main__":
    play_game()
