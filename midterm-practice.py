
import numpy as np
import scipy
import scipy.linalg

A: np.ndarray = np.array([[0, 1, 2],
                          [2, 4, 4],
                          [1, 1, 1]])

factorization = scipy.linalg.lu_factor(A)

print(factorization[0])
