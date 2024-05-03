
import numpy as np
import math

def compute_n_terms(total_events:int) -> dict[str: any]:
    '''
        Auxiliary calculator for EVENTS problem 1b in Homework 2

        return:
        
        calculates the number of terms in continuing the conversation joint probability expansion
        given only one condition can be applied per term

        n! terms exist for the regular expansion so this should yield more than that
    '''

    arr = np.array([1])

    for i in range(2, total_events + 1):

        arr = np.append(arr, math.comb(i, 2))

    # return np.sum(arr)
    # return math.factorial(np.sum(arr))

    return {
        'terms': math.factorial(np.sum(arr)),
        'large_enough': math.factorial(np.sum(arr)) > math.factorial(total_events)
    }

print(compute_n_terms(5))
