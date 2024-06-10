''' script to generate some random tic tac toe game data for n games '''

import random
import numpy as np

game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # vector of 9 empty elements
print(len(game_board))
entry = 1

for turn in range(len(game_board)):
    
    spot = random.randint(0, len(game_board) - 1)
    print(spot)
    print(game_board[spot])

    while game_board[spot] != ' ':
        spot = random.randint(0, len(game_board) - 1)

    game_board[spot] = entry

    entry *= -1
    
print(game_board)   # test to be sure the board filled properly

print(np.array(game_board).reshape(3, 3))   # visualize on a 3 x 3 grid


''' the above works, let's create a function to simulate 1000 games '''

def create_game_data(n_runs: int) -> np.ndarray:
    ...
