from TicTacToe import create_board, choose_starting_player, switch_player, get_available_moves
from unittest.mock import patch

def test_create_board():
    """ 
    test if the board is correctly initialized 
    """
    exp_board = create_board()
    assert len(exp_board) == 9
    assert exp_board == [' '] * 9

@patch('random.choice', return_value='X')
def test_choose_starting_player(mock_choice):
    """ 
    test if the player X is randomly selected 
    """
    assert choose_starting_player() == 'X'
    mock_choice.assert_called_once_with(['X', 'O'])


def test_switch_player():
    assert switch_player('X') == 'O'
    assert switch_player('O') == 'X'

def test_get_available_moves():
    board = create_board()
    moves = get_available_moves(board)
    assert len(moves) == 9
    board[0] = 'X'
    board[1] = 'O'
    board[2] = 'X'
    moves = get_available_moves(board)
    assert len(moves) == 6
    assert 0 not in moves
    assert 1 not in moves
    assert 2 not in moves