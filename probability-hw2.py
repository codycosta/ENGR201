
'''

Problem Statement:

We noted that the conventional accuracy measure — the ratio of TN + TP to the
total cases is not always a revealing measure of test performance. Simulate the
accuracy and precision for the current confusion matrix as prevalence varies from
0 to 1, and plot the results.

Terms to define:

Accuracy    = sum of diagonal / total count
Precision   = PPV = TP / ( TP + TN )
Prevalence  = P(True)

'''

import numpy as np
import matplotlib.pyplot as plt

total_population: int = 100

PREVALENCE = np.linspace(0, 1, 101)
# print(prevalence)


# as prevalence increases from 0 to 1 we need to generate a new matrix of values at each step

def generate_matrix(prevalence) -> np.ndarray:

    ''' 
    matrix scheme is as such:

                P   N
               _______
        True  | TP  FN  sum = prev * total_pop
        False | FP  TN  
    '''
    try:
        # generate a random number of true and false values to fill the matrix

        if prevalence == 0:
            FP = np.random.randint(0, total_population)
            TN = total_population - FP

            return np.array([[0, 0],
                            [FP, TN]])
        
        if prevalence == 1:
            TP = np.random.randint(0, total_population)
            FN = total_population - TP

            return np.array([[TP, FN],
                             [0, 0]])

        total_true = prevalence * total_population  # TP + FN
        TP = np.random.randint(0, total_true)
        FN = total_true - TP

        total_false = total_population - total_true # FP + TN
        FP = np.random.randint(0, total_false)
        TN = total_false - FP

        return np.array([[TP, FN],
                        [FP, TN]])

    except ValueError:
        print(f'{prevalence} caused an error')


# calculate needed accuracy and precision values to plot for each matrix

def calculate_accuracy_and_precision(matrix) -> dict[str: float]:

    '''
    Reminder:

        Accuracy    = sum of diagonal / total count
        Precision   = PPV = TP / ( TP + TN )
    '''

    accuracy = (matrix[0, 0] + matrix[1, 1]) / np.sum(matrix)
    precision = matrix[0, 0] / (matrix[0, 0] + matrix[1, 1])

    return {
        'accuracy': accuracy,
        'precision': precision
    }



# main procedure to generate plot

accuracy = []
precision = []


plt.title('Plot of accuracy and precision for prevalence = [0...1]')


for idx, p in enumerate(PREVALENCE):

    m = generate_matrix(round(p, 2))
    output = calculate_accuracy_and_precision(m)

    accuracy.append(output['accuracy'])
    precision.append(output['precision'])

    plt.plot(PREVALENCE[:idx], accuracy[:idx], PREVALENCE[:idx], precision[:idx], marker='o')
    plt.pause(0.1)


plt.plot(PREVALENCE, np.poly1d(np.polyfit(PREVALENCE, accuracy, 1))(PREVALENCE))
plt.plot(PREVALENCE, np.poly1d(np.polyfit(PREVALENCE, precision, 1))(PREVALENCE))

plt.legend(['accuracy', 'precision', 'accuracy trend', 'precision trend'])

plt.show()
