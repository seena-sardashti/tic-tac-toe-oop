import os
from src.board import *
from src.player import *
from src.game import *

#COMMANDS

def build_board():
    board = Board()
    return board
def build_game():
    player_X = Player('X')
    player_O = Player('O')
    board = build_board()
    new_game = Game(board, player_X, player_O)
    return play_game(new_game)


def play_game(game):
        # board = Board() #create connection with Board() and Game()
        
        def print_header():
            print("Welcome to tic-tac-toe\n")

        def refresh_screen():
            os.system("clear")
            print_header()
            game.board.display()

        while True:
            refresh_screen()

            #get x input - instantiate a Player() instance
            #make the choice a Player() function?
            player_X = Player('X')
            x_choice = int(input(f"\n{player_X.symbol}) Please choose 1-9. >"))
            #game.player_x_moves = Move(x_choice)

            #update board
            game.board.update_space(x_choice, "X")

            refresh_screen()

            #check X winner
            if game.board.is_winner("X"):
                print("\nX is winner\n")
                game.player_X.score += 1
                print(f"player {game.player_X.symbol} score is {game.player_X.score}")
                play_again = input("Would you like to play again (Y/N)").upper()
                if play_again == "Y":
                    build_game() #change to build_game()
                    continue
                else:
                    break
                    
            
            if game.board.is_tie():
                print("\ntie game\n")
                play_again = input("Would you like to play again (Y/N)").upper()
                if play_again == "Y":
                    build_game() #change to build_game()
                    continue
                else:
                    break

            #get o input - instantiate a Player() instance
            player_O = Player('O')
            o_choice = int(input(f"\n{player_O.symbol}) Please choose 1-9. >"))

            #update board - create an action class
            game.board.update_space(o_choice, "O")

            #check O winner
            if game.board.is_winner("O"):
                print("\nO is winner\n")
                game.player_O.score += 1
                print(f"player {game.player_O.symbol} score is {game.player_O.score}")
                play_again = input("Would you like to play again (Y/N)").upper()
                if play_again == "Y":
                    build_game() #change to build_game()
                    continue
                else:
                    break
            
            if game.board.is_tie():
                print("\ntie game\n")
                play_again = input("Would you like to play again (Y/N)").upper()
                if play_again == "Y":
                    build_game() #change to build_game()
                    continue
                else:
                    break