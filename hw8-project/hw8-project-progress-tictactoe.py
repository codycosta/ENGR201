
import random


boxes = [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]
HUMAN = 'X'
COMPUTER = '0'
first_player = HUMAN
turn = 1
winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                  [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def print_board(initial=False):
    """ Print the game board. If this is the beginning of the game,
        print out 1-9 in the boxes to show players how to pick a
        box. Otherwise, update each box with X or 0 from boxes[].
    """
    print(('''
             {} | {} | {} 
            -----------
             {} | {} | {}
            -----------
             {} | {} | {} 
        ''').format(*([x for x in range(1, 10)] if initial else boxes)))


def take_turn(player, turn):
    """ Create a loop that keeps asking the current player for
        their input until a valid choice is made.
    """

    while True:
        if player is COMPUTER:
            box = get_computer_move()
        else:
            box = input('Player %s, type a number from 1-9 to select a box: ' % player)

            try:
                box = int(box) - 1 # subtract 1 to sync with boxes[] index numbers
            except ValueError:
                # Not an integer
                print('That\'s not a valid number, try again.\n')
                continue

        if box < 0 or box > 8:
            print('That number is out of range, try again.\n')
            continue

        if boxes[box] == ' ': # initial value
            boxes[box] = player # set to value of current player
            break
        else:
            print('That box is already marked, try again.\n')


def get_computer_move():
    """ Return a random integer from 0 to 8, inclusive
    """
    return random.randint(0,8)
        

def switch_player(turn):
    """ Switch the player based on how many moves have been made.
        X starts the game so if this turn # is even, it's 0's turn. 
    """
    current_player = COMPUTER if turn % 2 == 0 else HUMAN
    return current_player


def check_for_win(player, turn):
    """ Check for a win (or a tie). For each combo in winning_combos[],
        count how many of its corresponding squares have the current 
        player's mark. If a player's score count reaches 3, return a win.
        If it doesn't, and this is already turn # 9, return a tie. If
        neither, return False so the game continues.
    """
    if turn > 4: # need at least 5 moves before a win is possible
        for combo in winning_combos:
            score = 0
            for index in combo:
                if boxes[index] == player:
                    score += 1
                if score == 3:
                    return 'win'

        if turn == 9:
            return 'tie'


def play(player, turn):
    """ Create a loop that keeps the game in play
        until it ends in a win or tie
    """
    while True:
        take_turn(player, turn)
        print_board()
        result = check_for_win(player, turn)
        if result == 'win':
            print('Game over. %s wins!\n' % player)
            break
        elif result == 'tie':
            print('Game over. It\'s a tie.\n')
            break
        turn += 1
        player = switch_player(turn)


# Begin the game: 
print('\n\nWelcome to Tic Tac Toe for two humans!')
print_board(initial=False)
play(first_player, turn)
