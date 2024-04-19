''' 

    probability hw qeustion, plotting distribution of n choose k:
    
    compute n choose k for n = 0 ... 6, 0 <= k <= n and plot to create pascal's triangle
    plot the value of n choose k for each value of n

'''

import numpy as np
import matplotlib.pyplot as plt
import math

# let's make the x axis k, and the y axis nchoosek, and we will include the value n in the legend as a denoter

upper_limit = 6    # change this to edit the sample size of the graphs

legends = []


n = np.array([i for i in range(upper_limit + 1)])

for num in n:

    legends.append(f'n = {num}')

    nchoosek = np.array([math.comb(num, el) for el in n[ : num + 1]])

    plt.plot(n[ : num + 1] ,nchoosek, marker='o')


# design our plot

plt.xlabel('k')
plt.ylabel('n choose k')
plt.legend(legends)
plt.title(f'Plots of comb(n, k) for values n,k <= {upper_limit}')

plt.show()
