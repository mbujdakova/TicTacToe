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

def make_move(board, move, player):
    board[move] = player

def player_move(board, player):
    moves = get_available_moves(board)
    move = random.choice(moves)
    make_move(board, move, player)
    return move

def check_win(board):
    winning_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                         [0, 3, 6], [1, 4, 7], [2, 5, 8],
                         [0, 4, 8], [2, 4, 6]]

    for position in winning_positions:
        if board[position[0]] == board[position[1]] == board[position[2]] != ' ':
            return board[position[0]] if board[position[0]] != ' ' else None
    if ' ' not in board:
        return 'Draw'

def render_board(board):
    row1 = " {} | {} | {} ".format(board[0], board[1], board[2])
    row2 = " {} | {} | {} ".format(board[3], board[4], board[5])
    row3 = " {} | {} | {} ".format(board[6], board[7], board[8])
    divider = "---+---+----"
    board_with_grid = "\n".join([row1, divider, row2, divider, row3])
    return board_with_grid

def initialize_game():
    board = create_board()
    print("Game Board Creation...\n")
    print(render_board(board))
    print("\nBoard Created.")
    return board 

