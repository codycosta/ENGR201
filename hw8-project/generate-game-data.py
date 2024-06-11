''' script to generate some random tic tac toe game data for n games played at complete random, no thinking by computers involved '''

import numpy as np
import matplotlib.pyplot as plt


''' the above works, let's create a function to simulate 1000 or so games '''

def create_game_data(n_runs: int) -> tuple:
    
    ''' in this case lets assign X to be 1 and O to be -1, not that it really matters lol '''
    
    ''' returns a tuple of arrays --> (game board data, recorded win combos)'''

    output = None
    entry = 1
    wins_data = np.zeros(8)

    for simulation in range(n_runs):

        entry *= -1 # alternate who starts each game

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
            
                for idx, combo in enumerate(winning_combos):

                    if game_board[combo[0]] and game_board[combo[1]] and game_board[combo[2]]:
                        if game_board[combo[0]] == game_board[combo[1]] == game_board[combo[2]]:

                            win = True
                            wins_data[idx] += 1
                            break
            
            if win:
                break


        if simulation == 0:
            output = game_board

        else:
            output = np.vstack([output, np.array(game_board)])


    return (output, wins_data)


for n in range(4):
    data = create_game_data(10000)
    board_data = data[0]
    wins_data = data[1]

    # print(data[0].reshape(3, 3))
    # print(np.sum(wins_data))

    plt.plot(wins_data)
plt.title('Instances of each win combination')

plt.show()


''' reuslts show by random chance that winning_combos 7 and 8 (last 2 entries) appear the most, at about 15% each
    the rest of the entries appear between 5 to 10% of the time
     
    since random analysis prefers these 2 combos over the rest, we can make the computer seek to win via these combos '''
