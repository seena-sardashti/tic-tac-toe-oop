from src.board import *
from src.player import *
from src.game import *
from src.index import *
from src.match_player import *

# board = Board()
# # game_one = Game(board)

# def play_game(board):
#         # board = Board() #create connection with Board() and Game()
#         def print_header():
#             print("Welcome to tic-tac-toe\n")

#         def refresh_screen():
#             os.system("clear")
#             print_header()
#             board.display()

#         while True:
#             refresh_screen()

#             #get x input - instantiate a Player() instance
#             #make the choice a Player() function?
#             player_X = Player('X')
#             x_choice = int(input(f"\n{player_X.symbol}) Please choose 1-9. >"))

#             #update board
#             board.update_space(x_choice, "X")

#             refresh_screen()

#             #check X winner
#             if board.is_winner("X"):
#                 print("\nX is winner\n")
#                 play_again = input("Would you like to play again (Y/N)").upper()
#                 if play_again == "Y":
#                     board.reset_board()
#                     continue
#                 else:
#                     break
            
#             if board.is_tie():
#                 print("\ntie game\n")
#                 play_again = input("Would you like to play again (Y/N)").upper()
#                 if play_again == "Y":
#                     board.reset_board()
#                     continue
#                 else:
#                     break

#             #get o input - instantiate a Player() instance
#             player_O = Player('O')
#             o_choice = int(input(f"\n{player_O.symbol}) Please choose 1-9. >"))

#             #update board - create an action class
#             board.update_space(o_choice, "O")

#             #check O winner
#             if board.is_winner("O"):
#                 print("\nO is winner\n")
#                 play_again = input("Would you like to play again (Y/N)").upper()
#                 if play_again == "Y":
#                     board.reset_board()
#                     continue
#                 else:
#                     break
            
#             if board.is_tie():
#                 print("\ntie game\n")
#                 play_again = input("Would you like to play again (Y/N)").upper()
#                 if play_again == "Y":
#                     board.reset_board()
#                     continue
#                 else:
#                     break
