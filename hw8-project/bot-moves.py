''' script to intelligently make computer moves during tic tac toe games
    scales with difficulty '''

import random

def easy_computer_move():
    ''' computer picks a random open space to place an X or O, no thinking needed '''

    return random.randint(0,8)


def medium_computer_move():
    ''' computer thinks a little more about where to put their next move, can still be beat '''
    ...


def hard_computer_move():
    ''' computer actively tries to win '''
    ...

