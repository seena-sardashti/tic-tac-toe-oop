
from src.player import *
from src.game import *
from src.index import *

class Board:
    def __init__(self):
        
        self.spaces = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    def display(self):
        print (" %s | %s | %s " %(self.spaces[1], self.spaces[2], self.spaces[3]))
        print("------------")
        print (" %s | %s | %s " %(self.spaces[4], self.spaces[5], self.spaces[6]))
        print("------------")
        print (" %s | %s | %s " %(self.spaces[7], self.spaces[8], self.spaces[9]))
    def update_space(self, space_no, player): # create an action class
        if self.spaces[space_no] == " ": #change to game.board.spaces
            self.spaces[space_no] = player
    def is_winner(self, player): #3rd position, minus 2nd postion == 2nd position minus 1st position
        #1st position minus 2nd position = 2nd position minus 3rd position
        if self.spaces[1]==player and self.spaces[2]==player and self.spaces[3]==player:
            return True
        if self.spaces[4]==player and self.spaces[5]==player and self.spaces[6]==player:
            return True
        if self.spaces[7]==player and self.spaces[8]==player and self.spaces[9]==player:
            return True
        if self.spaces[1]==player and self.spaces[4]==player and self.spaces[7]==player:
            return True
        if self.spaces[2]==player and self.spaces[5]==player and self.spaces[8]==player:
            return True
        if self.spaces[3]==player and self.spaces[6]==player and self.spaces[9]==player:
            return True
        if self.spaces[1]==player and self.spaces[5]==player and self.spaces[9]==player:
            return True
        if self.spaces[3]==player and self.spaces[5]==player and self.spaces[7]==player:
            return True
    def is_tie(self):
        used_spaces = 0
        for space in self.spaces:
            if space != " ":
                used_spaces += 1
        if used_spaces == 9:
            return True
        else:
            return False
    # def reset_board(self):
    #     self.spaces = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]



   

