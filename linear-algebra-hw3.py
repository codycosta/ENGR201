
import numpy as np
import sys


def generate_random_matrix(size: int, type: str) -> np.ndarray:

    '''
        Return:

        Function will return a square matrix of shape: (size, size)

        The type will specify the format of the matrix:

        d = diagonal
        t = upper triangular
        s = symmetric    
    '''

    matrix = np.zeros([size, size])

    if type == 'd':

        for j in range(size):
            matrix[j, j] = np.random.randint(0, 100)

        return matrix
    
    elif type == 't':

        for j in range(size):
            matrix[j, j:] = np.array([np.random.randint(0, 100) for j in range(size - j)])

        return matrix

    elif type == 's':

        m = generate_random_matrix(size, 'd')
        # symmetries = size - 1

        for j in range(size):
            random_filler = np.array([np.random.randint(0, 100) for j in range(size - j - 1)])

            m[j, j+1:] = random_filler
            m[j+1:, j] = random_filler

        # if m == m.T:

        return m
        


def commute_matrices(m1: np.ndarray, m2: np.ndarray) -> bool:
    
    '''
        Return:
        
        Intakes 2 matrices and checks for commutativity, returns a boolean
    '''

    if np.sum(m1 @ m2 == m2 @ m1) == m1.shape[0] * m1.shape[1]:
        return True
    
    return False



# test commutativity of diagonal matrices

# diagonal_m1 = np.array([[6, 0],
#                         [0, 21]])

# diagonal_m2 = np.array([[4, 0],
#                         [0, 7]])

# print(commute_matrices(diagonal_m1, diagonal_m2))

# print(commute_matrices(generate_random_matrix(10, 'd'), generate_random_matrix(10, 'd')))
# print(commute_matrices(generate_random_matrix(10, 't'), generate_random_matrix(10, 't')))
# print(commute_matrices(generate_random_matrix(10, 's'), generate_random_matrix(10, 's')))

# m = generate_random_matrix(10, 'd')
# print(m)



def main() -> None:

    size: int = int(sys.argv[1])

    print('\nEvaluating matrix commutativity:\n')

    print(f'diagonal:\t{commute_matrices(generate_random_matrix(size, 'd'), generate_random_matrix(size, 'd'))}')
    print(f'triangular:\t{commute_matrices(generate_random_matrix(size, 't'), generate_random_matrix(size, 't'))}')
    print(f'symmetric:\t{commute_matrices(generate_random_matrix(size, 's'), generate_random_matrix(size, 's'))}')



main()
