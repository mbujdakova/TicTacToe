import random
def create_board():
    board = [' '] * 9
    return board

def choose_starting_player():
    return random.choice(['X', 'O'])

def switch_player(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'

def get_available_moves(board):
    moves = []
    for i in range(len(board)):
        if board[i] == ' ':
            moves.append(i)
    return moves

def player_move(board, player):
    moves = get_available_moves(board)
    move = random.choice(moves)
    board[move] = player
    return move

