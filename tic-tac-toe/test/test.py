from TicTacToe import create_board, choose_starting_player, switch_player, get_available_moves, player_move, make_move
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
    """ 
    check if the available moves of empty board are 9
    """
    board = create_board()
    available_moves  = get_available_moves(board)
    assert len(available_moves) == 9

    """ 
    check if the available moves of board with moves in 0., 1. and 2. postion is 6 and if 0,1 and 2 are not present in available moves
    """
    board[0] = 'X'
    board[1] = 'O'
    board[2] = 'X'
    available_moves = get_available_moves(board)
    assert len(available_moves ) == 6
    assert 0 not in available_moves 
    assert 1 not in available_moves 
    assert 2 not in available_moves 

@patch('random.choice', return_value=4)
def test_player_move(mock_choice):
    board = ['O', 'X', 'O', ' ', ' ', 'X', ' ', ' ', 'X']
    player = 'X'
    exp_move = player_move(board, player)
    assert board == ['O', 'X', 'O', ' ', 'X', 'X', ' ', ' ', 'X']
    assert exp_move == 4

def test_make_move():
    board = ['X', 'O', 'X', 'O', ' ', ' ', ' ', ' ', ' ']
    move = 4
    player = 'X'
    make_move(board, move, player)
    assert board == ['X', 'O', 'X', 'O', 'X', ' ', ' ', ' ', ' ']

