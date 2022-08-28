from src.board import *

def test_if_board():
    state = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    board = Board()
    assert board == state
def test_if_board_updated():
    board = Board()
    board.update_space(1, "O")
    assert board == ["O", " ", " ", " ", " ", " ", " ", " ", " ", " "]
def test_if_player_class_created():
    #test if player class is defined
    pass
def test_if_player_class_uploaded_to_store():
    #test if player class instance saved to store
    pass
def test_if_input_updates_board():
    #test if a method uses a user input
    pass