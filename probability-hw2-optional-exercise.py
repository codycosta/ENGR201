
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

# total_population: int = 100

# PREVALENCE = np.linspace(0, 1, 101)



# as prevalence increases from 0 to 1 we need to generate a new matrix of values at each step

def generate_random_matrix(prevalence: int, total_population: int) -> np.ndarray:

    ''' 
        matrix scheme is as such:

                P   N
               _______
        True  | TP  FN  sum = prev * total_pop
        False | FP  TN  


        Return:

        This function will fill the values of TP and FN with random integers 
        such that the sum matches the desired prevalence of the matrix


        Results:

        Generating this matrix with random values each time did not provide the
        desired results shown in class

        Will need to take a different approach

        This function is still usable to create the base case of 0 prevalence however
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



# as prevalence increases from 0 to 1 we need to modify the values of the matrix at each step

def increment_matrix(m: np.ndarray) -> np.ndarray:

    '''
        Reminder:

        matrix scheme is as such:

                P   N
               _______
        True  | TP  FN  sum = prev * total_pop
        False | FP  TN  


        Return:

        This function will pass a matrix 'm' as an argument and
        decrement the values of FP and TP, while incrementing the 
        values of TP and FN

        This essentially will create less random behavior between
        each iteration of the prevalence of interest


    '''

    FP = m[1, 0]
    TN = m[1, 1]

    # # check for existing values within the bottom row of the matrix
    # # increment/decrement if values exist

    # if FP and TN:
    #     TP += 1
    #     FN += 1

    #     FP -= 1
    #     TN -= 1

    # elif FP and not TN:
    #     TP += 1
    #     FP -= 1

    # elif TN and not FP:
    #     FN += 1
    #     TN -= 1

    # # if both TN and FP are 0 then prevalence = 1 and we are done

    # elif not TN and not FP:
    #     return np.array([[0, 0],
    #                      [0, 0]])
    
    # return np.array([[TP, FN],
    #                  [FP, TN]])

    if FP and TN:
        m[1, np.random.randint(0, 2)] -= 1  # random decrement
        m[0, np.random.randint(0, 2)] += 1  # random increment

    elif FP and not TN:
        m[1, 0] -= 1
        m[0, np.random.randint(0, 2)] += 1  # random increment
    
    elif TN and not FP:
        m[1, 1] -= 1
        m[0, np.random.randint(0, 2)] += 1  # random increment

    elif not TN and not FP:
        return np.array([[0, 0],
                         [0, 0]])


    return m



# calculate needed accuracy and precision values to plot for each matrix

def calculate_accuracy_and_precision(matrix: np.ndarray) -> dict[str: float]:

    '''
        Reminder:

        Accuracy    = sum of diagonal / total count
        Precision   = PPV = TP / ( TP + TN )

        Return:
        
        Values for the precision and accuracy of the confusion matrix
    '''

    accuracy = (matrix[0, 0] + matrix[1, 1]) / np.sum(matrix)
    precision = matrix[0, 0] / (matrix[0, 0] + matrix[1, 1])

    return {
        'accuracy': accuracy,
        'precision': precision
    }



def generate_average_plot_of_n_trials(trials: int) -> None:
    
    '''
        Return:

        creates a plot of the average performance of the precision
        and accuracy over a set number of trials

    '''

    initial_result = main()

    prevalence = initial_result['prevalence']

    precision = initial_result['precision']
    accuracy = initial_result['accuracy']

    
    n = 1

    while n < trials:
        
        trial_result = main()

        # if not ave_precision.shape[0]:
        #     ave_precision = np.append(ave_precision, trial_result['precision'])

        # if not ave_accuracy.shape[0]:
        #     ave_accuracy = np.append(ave_accuracy, trial_result['accuracy'])

        precision = np.vstack([precision, trial_result['precision']])
        accuracy = np.vstack([accuracy, trial_result['accuracy']])

        n += 1
    

    # print(precision.shape)  # shape is correct

    # flatten array into one vector of all column averages

    ave_precision = precision.mean(axis=0)

    plt.plot(prevalence, ave_precision)
    plt.show()




# main procedure to generate plot

def main_old() -> None:

    PREVALENCE = np.linspace(0, 1, 101)
    population: int = 100

    accuracy = []
    precision = []


    plt.title('Plot of accuracy and precision for prevalence = [0...1]')


    for idx, p in enumerate(PREVALENCE):

        m = generate_random_matrix(round(p, 2), population)
        output = calculate_accuracy_and_precision(m)

        accuracy.append(output['accuracy'] * 100)
        precision.append(output['precision'] * 100)

        plt.plot(PREVALENCE[:idx], accuracy[:idx], PREVALENCE[:idx], precision[:idx], marker='o')
        plt.pause(0.05)


    plt.plot(PREVALENCE, np.poly1d(np.polyfit(PREVALENCE, accuracy, 1))(PREVALENCE))
    plt.plot(PREVALENCE, np.poly1d(np.polyfit(PREVALENCE, precision, 1))(PREVALENCE))

    plt.legend(['accuracy', 'precision', 'accuracy trend', 'precision trend'])
    plt.xlabel('Prevalence')
    plt.ylabel('Metric (%)')
    plt.show()



def main() -> dict[str: np.ndarray]:

    population = 144
    precision = np.array([])
    accuracy = np.array([])

    matrix = generate_random_matrix(0, population)
    # print(matrix)

    while np.sum(matrix):

        precision = np.append(precision, calculate_accuracy_and_precision(matrix)['precision'])
        accuracy = np.append(accuracy, calculate_accuracy_and_precision(matrix)['accuracy'])

        matrix = increment_matrix(matrix)
        # print(precision)

    prevalence = np.linspace(0, 1, precision.shape[0])

    # plt.plot(prevalence, precision, prevalence, accuracy)

    # plt.title('Plot of accuracy and precision for prevalence = [0...1]')
    # plt.legend(['precision', 'accuracy'])
    # plt.xlabel('Prevalence')
    # plt.ylabel('Metric (%)')
    # plt.show()

    # print(precision.shape)

    return {
        'precision': precision,
        'accuracy': accuracy,
        'prevalence': prevalence
    }



# main_old()
main()

generate_average_plot_of_n_trials(200)
