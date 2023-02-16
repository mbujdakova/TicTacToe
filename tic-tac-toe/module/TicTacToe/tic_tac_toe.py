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