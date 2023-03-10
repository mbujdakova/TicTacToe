from TicTacToe import create_board, choose_starting_player, switch_player, get_available_moves, player_move, make_move, check_win, render_board, initialize_game, play_game
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
    """
    test the randomly chosen move 4 of user X using patch and see the expected move and resulting board 
    """
    board = ['O', 'X', 'O', ' ', ' ', 'X', ' ', ' ', 'X']
    player = 'X'
    exp_move = player_move(board, player)
    assert board == ['O', 'X', 'O', ' ', 'X', 'X', ' ', ' ', 'X']
    assert exp_move == 4

def test_make_move():
    """
    test move 4 of user X  see the resulting board 
    """
    board = ['X', 'O', 'X', 'O', ' ', ' ', ' ', ' ', ' ']
    move = 4
    player = 'X'
    make_move(board, move, player)
    assert board == ['X', 'O', 'X', 'O', 'X', ' ', ' ', ' ', ' ']

def test_check_win():
    """
    check the win for 4 possible scenarios 
    """
    #initialization (empty board)
    board = create_board()
    assert check_win(board) is None

    #vertical win
    board = ['X', ' ', ' ', 
             'X', 'O', ' ',
             'X', ' ', 'O']
    assert check_win(board) == 'X'

    # horizontal win
    board = ['X', ' ', 'X', 
             'O', 'O', 'O',
             'X', ' ', ' ']
    assert check_win(board) == 'O'


    #diagonal win
    board = ['X', ' ', ' ', 
             'O', 'X', ' ',
             'O', ' ', 'X']
    assert check_win(board) == 'X'

    board = ['X', 'O', 'X', 
             'O', 'O', 'X', 
             'X', 'X', 'O']
    assert check_win(board) == 'Draw'

def test_render_board():
    """
    test the result of render_board function with filled postions in board 
    """
    board = ['X', 'O', 'X', 
             'O', 'X', 'O', 
             'X', 'O', 'X']
    expected_output = " X | O | X \n---+---+----\n O | X | O \n---+---+----\n X | O | X "
    assert render_board(board) == expected_output

def test_initialize_game(capsys):
    """
    test the printed result of the inizialization of the game
    """
    expected_output = "Game Board Creation...\n\n   |   |   \n---+---+----\n   |   |   \n---+---+----\n   |   |   \n\nBoard Created.\n"
    board = initialize_game()
    captured_output = capsys.readouterr().out
    assert captured_output == expected_output

def test_play_game(capsys):
    """
    test if the final verdict is present in captured output of the play_game function 
    """
    play_game()
    out, err = capsys.readouterr()
    output = out.replace('\n', '')
    assert ("PLAYER X WON!" in output) or ("PLAYER O WON!" in output) or ("GAME ENDS WITH A DRAW!" in output)
