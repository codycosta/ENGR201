''' medium level bot to play tic tac toe, will defend but not play offense when given the choice '''

import numpy as np
import matplotlib.pyplot as plt

# boxes = [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]

# def print_board(game_board):
#     print(game_board.reshape(3, 3), '\n')

def print_board(game_board):
    """ Print the game board """

    output = []
    for x in game_board:
        if x > 0:
            output.append('X')
        elif x < 0:
            output.append('O')
        else:
            output.append(' ')

    print(('''
             {} | {} | {} 
            --------------
             {} | {} | {}
            --------------
             {} | {} | {} 
        ''').format(*([x for x in output])))
    

winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                  [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

''' from generate-game-data.py, the computers finished with a win in combos 7 and 8, 
    so let's reverse the order of the list to check for possible wins with these combos first '''

winning_combos.reverse()
# print(winning_combos)
    

game_board = np.zeros(9)
    
entry = 1
win = False
    
for turn in range(9):

    '''' check for imminent win '''

    for combo in winning_combos:

        # win_possible = False
        # win_com = None

        # if you are about to win, play some O

        if game_board[combo[0]] + game_board[combo[1]] + game_board[combo[2]] == 2 * entry:

            ''' find empty spot '''
            empty_spot = None

            idxs = [0, 1, 2]
            for val in idxs:
                if game_board[combo[val]] == 0:
                    empty_spot = val
                    break
            
            game_board[combo[empty_spot]] = entry
            entry *= -1
            break
    
        # if opponent is about to win, play some D

        elif game_board[combo[0]] + game_board[combo[1]] + game_board[combo[2]] == -2 * entry:

            ''' find empty spot '''
            empty_spot = None

            idxs = [0, 1, 2]
            for val in idxs:
                if game_board[combo[val]] == 0:
                    empty_spot = val
                    break
            
            game_board[combo[empty_spot]] = entry
            entry *= -1
            break
        

    else:


        spot = np.random.randint(0, 9)

        while game_board[spot]:
            spot = np.random.randint(0, 9)



        game_board[spot] = entry
        entry *= -1

    print_board(game_board)

    ''' check for win condition '''

    if turn >= 4:

        for combo in winning_combos:

            if game_board[combo[0]] and game_board[combo[1]] and game_board[combo[2]]:
                if game_board[combo[0]] == game_board[combo[1]] == game_board[combo[2]]:

                    win = True
                    break
    
    if win:
        break

