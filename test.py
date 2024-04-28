
import numpy as np
import matplotlib.pyplot as plt
import math


''' let's try to learn a bit of numpy here '''

# x = np.linspace(0, 2*np.pi, 100)

# plt.plot(x, np.sin(x), x, np.cos(x))
# plt.xlabel('time')
# plt.ylabel('sin(t)')
# plt.title('My First Graph')
# plt.legend(('sin(t)', 'cos(t)'))
# plt.show()

# y = np.array([[1, 2],
#               [3, 4]])

# z = np.array([[4, 3],
#               [2, 1]])

# calculates dot product
# w = y @ z
# print(w)

# performs element-wise multiplication
# print(y * z)


''' 

    probability hw qeustion, plotting distribution of n choose k:
    
    compute n choose k for n = 0 ... 6, 0 <= k <= n and plot to create pascal's triangle
    plot the value of n choose k for each value of n

'''

# let's make the x axis k, and the y axis nchoosek, and we will include the value n in the legend as a denoter

upper_limit = 6    # change this to edit the sample size of the graphs

legends = []


n = np.array(range(upper_limit + 1))

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


w = [x for x in [0, 1, 2, 3, 4, 5, 6] if x % 2 == 0]
