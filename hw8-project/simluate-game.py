
import numpy as np
import matplotlib.pyplot as plt

# boxes = [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]

def print_board(game_board):
    print(game_board.reshape(3, 3), '\n')

winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                  [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

winning_combos.reverse()
# print(winning_combos)
    

game_board = np.zeros(9)
    
entry = 1
win = False
    
for turn in range(9):

    '''' check for opponent imminent win '''

    for combo in winning_combos:

        win_possible = False
        win_com = None


        if game_board[combo[0]] + game_board[combo[1]] + game_board[combo[2]] == -2 * entry:

            win_possible = True
            win_com = combo
            break

    
    if win_possible:
        
        ''' find empty spot '''
        empty_spot = None

        idxs = [0, 1, 2]
        for val in idxs:
            if game_board[win_com[val]] == 0:
                empty_spot = val
                break
        
        game_board[win_com[empty_spot]] = entry
        entry *= -1


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



# print_board()
