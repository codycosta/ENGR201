''' script to generate some random tic tac toe game data for n games '''

import numpy as np
import matplotlib.pyplot as plt

# game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # vector of 9 empty elements
# print(len(game_board))
# entry = 1

# for turn in range(len(game_board)):
    
#     spot = np.random.randint(0, len(game_board) - 1)
#     print(spot)
#     print(game_board[spot])

#     while game_board[spot] != ' ':
#         spot = np.random.randint(0, len(game_board) - 1)

#     game_board[spot] = entry

#     entry *= -1
    
# print(game_board)   # test to be sure the board filled properly

# print(np.array(game_board).reshape(3, 3))   # visualize on a 3 x 3 grid


''' the above works, let's create a function to simulate 1000 or so games '''

def create_game_data(n_runs: int) -> np.ndarray:
    
    ''' in this case lets assign X to be 1 and O to be -1, not that it really matters lol '''

    output = None
    entry = 1

    for simulation in range(n_runs):

        game_board = np.zeros(9)  # vector of 9 empty elements
        win = False

        for turn in range(len(game_board)):

            spot = np.random.randint(0, 9)

            while game_board[spot]:
                spot = np.random.randint(0, 9)
            
            game_board[spot] = entry
            entry *= -1

            ''' check for win condition '''

            if turn >= 4:

                winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                                  [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
            
                for combo in winning_combos:
                    if game_board[combo[0]] and game_board[combo[1]] and game_board[combo[2]]:
                        if game_board[combo[0]] == game_board[combo[1]] == game_board[combo[2]]:
                            win = True
                            break
            
            if win:
                break


        if simulation == 0:
            output = game_board

        else:
            output = np.vstack([output, np.array(game_board)])


    return output


test_data = create_game_data(1000)

# for x in range(test_data.shape[0]):
#     print(test_data[x,:].reshape(3, 3), '\n')


''' let's analyze the data for any outstanding statistical significance by finding a distribution of common win combos '''

def evalute_game_wins(test_data) -> np.ndarray:

    winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                      [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    wins_data = np.zeros(8) # one space for each possibe win combo

    for game in range(test_data.shape[0]):

        current_game = test_data[game, :]

        for idx, combo in enumerate(winning_combos):
            
            if current_game[combo[0]] == current_game[combo[1]] == current_game[combo[2]]:
                wins_data[idx] += 1

    return wins_data



wins_data = evalute_game_wins(test_data)


plt.plot(wins_data)
plt.title('Instances of each win combination')
plt.show()
