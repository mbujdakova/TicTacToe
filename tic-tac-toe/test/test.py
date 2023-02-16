from TicTacToe import create_board 

def test_create_board():
    """ test if the board is correctly initialized """
    exp_board = create_board()
    assert len(exp_board) == 9
    assert exp_board == [' '] * 9
