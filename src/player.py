from src.board import *
from src.game import *
from src.index import *

class Player:
    def __init__(self, symbol = 'X' or 'O', score = 0):
        self.symbol = symbol
        player_id = len(store['players']) + 1
        self.id = player_id
        self.score = score
        store['players'][player_id] = self
        # self.store = store
        # player_id = len(store['players']) + 1
        # self.id = player_id
        # store['players'][player_id] = self
    
        
