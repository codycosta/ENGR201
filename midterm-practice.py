
import numpy as np
import scipy
import scipy.linalg as sl

A: np.ndarray = np.array([[1, 1, 1],
                          [1, 4, 4],
                          [1, 4, 8]])

factorization = sl.lu_factor(A)

# print(factorization[0])
# print(factorization[1])
# print(factorization)

# print(factorization[0] @ factorization[0])

I = np.eye(A.shape[0])
# print(I)

B: np.ndarray = np.array([[1, 2, 0, 1],
                          [0, 1, 1, 0],
                          [1, 2, 0, 1]])

# print(sl.lu_factor(B))


print(len(sl.lu(A)))
print('Permutation:\n', sl.lu(A)[0], '\n')
print('Lower:\n', sl.lu(A)[1], '\n')
print('Upper:\n', sl.lu(A)[2], '\n')

P, L, U = sl.lu(A)
