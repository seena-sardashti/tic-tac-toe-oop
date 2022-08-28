
from src.player import *
from src.board import *
from src.index import *

class Game:
    def __init__(self, board, player_X, player_O):
        self.board = board
        self.player_X = player_X
        self.player_O = player_O
        # self.player = player
        game_id = len(store['games']) + 1
        self.id = game_id
        # if player:
        #     self.player_id = player.id
        store['games'][game_id] = self
    def get_scores(self):
        player_X_scores = {k.self.player_X.scores for k in store['games'].values() if k == self.player_X}
        player_O_scores = {k.self.player_O.scores for k in store['games'].values() if k == self.player_O}
        return player_X_scores, player_O_scores
    # def play_game(self, board, player_X, player_O):
    #     # board = Board() #create connection with Board() and Game()
    #     def print_header():
    #         print("Welcome to tic-tac-toe\n")

    #     def refresh_screen():
    #         os.system("clear")
    #         print_header()
    #         self.board.display()

    #     while True:
    #         refresh_screen()

    #         #get x input - instantiate a Player() instance
    #         #make the choice a Player() function?
    #         player_X = Player('X')
    #         x_choice = int(input(f"\n{player_X.symbol}) Please choose 1-9. >"))

    #         #update board
    #         self.board.update_space(x_choice, "X")

    #         refresh_screen()

    #         #check X winner
    #         if self.board.is_winner("X"):
    #             print("\nX is winner\n")
    #             play_again = input("Would you like to play again (Y/N)").upper()
    #             if play_again == "Y":
    #                 self.board.reset_board()
    #                 continue
    #             else:
    #                 break
            
    #         if self.board.is_tie():
    #             print("\ntie game\n")
    #             play_again = input("Would you like to play again (Y/N)").upper()
    #             if play_again == "Y":
    #                 self.board.reset_board()
    #                 continue
    #             else:
    #                 break

    #         #get o input - instantiate a Player() instance
    #         player_O = Player('O')
    #         o_choice = int(input(f"\n{player_O.symbol}) Please choose 1-9. >"))

    #         #update board - create an action class
    #         self.board.update_space(o_choice, "O")

    #         #check O winner
    #         if self.board.is_winner("O"):
    #             print("\nO is winner\n")
    #             play_again = input("Would you like to play again (Y/N)").upper()
    #             if play_again == "Y":
    #                 self.board.reset_board()
    #                 continue
    #             else:
    #                 break
            
    #         if self.board.is_tie():
    #             print("\ntie game\n")
    #             play_again = input("Would you like to play again (Y/N)").upper()
    #             if play_again == "Y":
    #                 self.board.reset_board()
    #                 continue
    #             else:
    #                 break

    # def play_game(self):
    #     # board = Board() #create connection with Board() and Game()
    #     def print_header():
    #         print("Welcome to tic-tac-toe\n")

    #     def refresh_screen():
    #         os.system("clear")
    #         print_header()
    #         self.board.display()

    #     while True:
    #         refresh_screen()

    #         #get x input - instantiate a Player() instance
    #         #make the choice a Player() function?
    #         player_X = Player('X')
    #         x_choice = int(input(f"\n{player_X}) Please choose 1-9. >"))

    #         #update board
    #         self.board.update_space(x_choice, "X")

    #         refresh_screen()

    #         #check X winner
    #         if self.board.is_winner("X"):
    #             print("\nX is winner\n")
    #             play_again = input("Would you like to play again (Y/N)").upper()
    #             if play_again == "Y":
    #                 self.board.reset_board()
    #                 continue
    #             else:
    #                 break
            
    #         if self.board.is_tie():
    #             print("\ntie game\n")
    #             play_again = input("Would you like to play again (Y/N)").upper()
    #             if play_again == "Y":
    #                 self.board.reset_board()
    #                 continue
    #             else:
    #                 break

    #         #get o input - instantiate a Player() instance
    #         player_O = Player('O')
    #         o_choice = int(input(f"\n{player_O}) Please choose 1-9. >"))

    #         #update board - create an action class
    #         self.board.update_space(o_choice, "O")

    #         #check O winner
    #         if self.board.is_winner("O"):
    #             print("\nO is winner\n")
    #             play_again = input("Would you like to play again (Y/N)").upper()
    #             if play_again == "Y":
    #                 self.board.reset_board()
    #                 continue
    #             else:
    #                 break
            
    #         if self.board.is_tie():
    #             print("\ntie game\n")
    #             play_again = input("Would you like to play again (Y/N)").upper()
    #             if play_again == "Y":
    #                 self.board.reset_board()
    #                 continue
    #             else:
    #                 break
def start_game():
    print('Please ') 

#  class Game:
#     def play_game(self):
#         #print welcome to tic-tac-toe and the board, and ask for player symbol
#         # instantiate classes with functions
#         print(f"welcome to tic-tac-toe")
        
#     def print_board(self):
#         board = build_store()['store']['state']
#         return print(f"here is the the board {board}")
        
#     def make_move(self):
#         board = build_store()['store']['state']
#         print(f"player, are you X or O?")
#         player_symbol = input()
#         player = Player(self, board, player_symbol)
#         print(f"{player.symbol} your turn, enter the space you'd like to move")
#         symbol = player.symbol
#         turn = 0
#         for i in range(10):
#             self.print_board()
#             print(f"It's your turn {self.player.symbol}, what space would you move?")
#             move = input()

#             if board[move] == '':
#                 board[move] = symbol
#                 turn += 1
#             else:
#                 print(f"space already taken")
#                 continue
    
