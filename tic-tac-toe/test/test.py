from TicTacToe import create_board, choose_starting_player, switch_player
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

    