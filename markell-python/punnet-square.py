
# dominant and recessive gene simulation with user inputs
from helper_functions import *

# define gene list
dominant = ['c', 'cleft chin', 'widow\'s peak', 'dimples', 'brown/black hair', 'freckles', 'brown eyes', 'free earlobe']
recessive = ['n', 'no cleft', 'no widow\'s peak', 'no dimples', 'blonde hair', 'no freckles', 'gray/blue eyes', 'attached earlobe']

# get control flow and repetitions from user
method: str = decide_control_flow()
repetitions: int = decide_repetitions()

# using primary for loop
if method == 'for':

    for j in range(repetitions):

        main_procedure(dominant, recessive)

        if repetitions > 1 and j != repetitions - 1:
            ask_to_proceed()


# using primary while loop
elif method == 'while':

    j = 0

    while j < repetitions:
    
        main_procedure()

        if repetitions > 1 and j != repetitions - 1:
            ask_to_proceed()

        j += 1
    