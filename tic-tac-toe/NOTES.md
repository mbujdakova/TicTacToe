The system should run in BOT mode (random BOT moves for player X & O) to print on the screen all the 
player's moves (with a 2 seconds timeout between each round) until someone won or the game ends with 
a draw

Pomodoro 1:

[x] create function for creating empty board (9 empty ' ')
    [x] test - check expected board and length of the list 
[x] create function  choose_starting_player() for randomly chosen first player (X or O)
    [x] test for function

Pomodoro 2:

[x] create function for switching players
        eg. input - 'X'
            output - 'O'
    [x] test for the switching players function 
[x] create function for checking the available moves (free spots)
            input - board (as a list)
            output - list with indexes of free spots in board
[] create function for randomly chosen move from list of free spots

Pomodoro 3:
[x] create function for randomly chosen move from list of free spots
    [x] test
[x] create function for making move (random move)
    [x] test 

Pomodoro 4:
[x] refactor code
[x] create a function for checking winner (with all possible scenarios)
    [x] test scenarios (horizontaly, vertically, draw)
[x] create function for rendering a board 

Pomodoro 5:
[x] implement logic of the game 
    - start with empty board 
    Game Board Creation... 
            | |  
            -+-+- 
            | |  
            -+-+- 
            | | 
            
    Board Created.
[] create function game which combines all functions
[] add sleeptime to the function
[] refactor 

Pomodoro 6:
[] create function game which combines all functions
    [] test the scenarios (draw or win of X/O)
[] add sleeptime to the function
[] refactor 