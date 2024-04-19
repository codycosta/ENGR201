import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

x = np.array([[0, 1, 2, 3], 
              [9, 8, 7, 6]])

# print(x[1,2])

'''this is cool!'''

# slope esitmator using numpy arrays

def slope(lower, upper):

    interval = np.array([lower, upper])
    values = interval * 8 - 1.86 * interval**2

    return np.round( (values[1] - values[0]) / (upper - lower), 2 )

def time_function_execution(func):
    start = time.time()
    func
    end = time.time()

    return print(f'function executed in {end - start} seconds')

# print(slope(1, 2))
# time_function_execution(slope(1, 2))


arr = np.array([[1, 2, 3], 
                [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)

x = x[x % 2 == 0]
print(x)
