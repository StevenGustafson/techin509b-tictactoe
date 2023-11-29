# logic.py

import csv

class TicTacToe:
    def record_winner(self, winner):
        with open('logs/winners_log.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([winner.number, winner.piece, winner.__class__.__name__])
    
    def undo_move(self, move):
        row, col = move
        self.board[row][col] = " "
        self.switch_player()

    def get_opponent(self, player):
        return self.player2 if player == self.player1 else self.player1
   
    def __init__(self, player1, player2):
        self.board = [[" "]*3 for _ in range(3)]
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1

    def reset_game(self):
        self.board = [[" "]*3 for _ in range(3)]
        self.current_player = self.player1

    def make_move(self, move):
        row, col = move
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player.piece
            self.switch_player()
            return True
        else:
            print("Invalid move. Try again.")
            return False

    def is_valid_move(self, row, col):
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == " " 

    def is_winner(self, player):
        for i in range(3):
            if all(self.board[i][j] == player.piece for j in range(3)) or all(self.board[j][i] == player.piece for j in range(3)):
                return True
            
        if all(self.board[i][i] == player.piece for i in range(3)) or all(self.board[i][2-i] == player.piece for i in range(3)):
            return True

        return False

    def is_draw(self):
        return all(cell != " " for row in self.board for cell in row)

    def switch_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def is_game_over(self):
        return self.is_winner(self.player1) or self.is_winner(self.player2) or self.is_draw()
    
    def get_random_valid_move(self):
        import random
        valid_moves = [(row, col) for row in range(3) for col in range(3) if self.is_valid_move(row, col)]
        return random.choice(valid_moves) if valid_moves else (0, 0)
    
    def get_game_result(self):
        if self.is_winner(self.player1):
            return "Player 1 wins!"
        elif self.is_winner(self.player2):
            return "Player 2 wins!"
        elif self.is_draw():
            return "It's a draw!"
        else:
            return "Game is not over yet."


class Player:
    def __init__(self, piece, number):
        self.piece = piece
        self.number = number

    def make_move(self, game):
        pass  # To be implemented in derived classes


class HumanPlayer(Player):
    # def make_move(self, game):
    #     row = int(input(f"Player {self.number}, enter the row (0, 1, or 2): "))
    #     col = int(input(f"Player {self.number}, enter the column (0, 1, or 2): "))
    #     move_result = game.make_move((row, col))
        
    #     if game.is_winner(self):
    #         game.record_winner(self)
            
    #     return move_result
    def make_move(self, game):
        row, col = game.get_random_valid_move()
        return game.make_move((row, col))



# logic.py

class BotPlayer(Player):
    # def make_move(self, game):
    #     _, move = self.minimax(game, self, game.get_opponent(self), float('-inf'), float('inf'))
    #     move_result = game.make_move(move)
    #     return move_result

    # def minimax(self, game, maximizing_player, minimizing_player, alpha, beta):
    #     if game.is_game_over():
    #         return self.evaluate(game), None

    #     available_moves = [(row, col) for row in range(3) for col in range(3) if game.is_valid_move(row, col)]

    #     if maximizing_player == self:
    #         best_score = float('-inf')
    #         best_move = None
    #         for move in available_moves:
    #             game.make_move(move)
    #             score, _ = self.minimax(game, game.get_opponent(self), self, alpha, beta)
    #             game.undo_move(move)

    #             if score > best_score:
    #                 best_score = score
    #                 best_move = move

    #             alpha = max(alpha, best_score)
    #             if alpha >= beta:
    #                 break  # Beta cut-off

    #         return best_score, best_move

    #     else:
    #         best_score = float('inf')
    #         best_move = None
    #         for move in available_moves:
    #             game.make_move(move)
    #             score, _ = self.minimax(game, self, game.get_opponent(self), alpha, beta)
    #             game.undo_move(move)

    #             if score < best_score:
    #                 best_score = score
    #                 best_move = move

    #             beta = min(beta, best_score)
    #             if alpha >= beta:
    #                 break  # Alpha cut-off

    #         return best_score, best_move

    # def evaluate(self, game):
    #     if game.is_winner(self):
    #         return 1
    #     elif game.is_winner(game.get_opponent(self)):
    #         return -1
    #     else:
    #         return 0
    def make_move(self, game):
        row, col = game.get_random_valid_move()
        return game.make_move((row, col))