
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

        Accuracy    = ( TP + TN ) / total count
        Precision   = PPV = TP / ( TP + TN )

        Return:
        
        Computes values for the precision and accuracy of the confusion matrix for a given prevalence

        
        Issue:

        Throws a RuntimeWarning for line:   precision = matrix[0, 0] / (matrix[0, 0] + matrix[1, 1])
        My assumption is that the diagonal of the matrix can proabilistically reach 0 or near 0 a small fraction of the time
        Across hundreds of simulations though, it becomes more likely

        Workaround is to increase the population (sample size) of the starting matrix
    '''

    try:

        accuracy = (matrix[0, 0] + matrix[1, 1]) / np.sum(matrix)
        precision = matrix[0, 0] / (matrix[0, 0] + matrix[1, 1])

        # return {
        #     'accuracy': accuracy,
        #     'precision': precision
        # }
    
    except RuntimeWarning:
        # print(precision)
        print(f'TP = {matrix[0, 0]}\tTN = {matrix[1, 1]}')

        # won't fucking print here, not sure why
    
    
    finally:

        return {
            'accuracy': accuracy,
            'precision': precision
        }



# fucntion to calculate data we want to plot later

def generate_performance_metrics_for_all_values_of_prevalence(population: int) -> dict[str: np.ndarray]:

    '''
        Return:

        Processes the cumulative performance of the matrix as prevalence increases from 0 to 1
        Returns a dictionary of arrays for precision, accuracy, and prevalence
    '''

    # population = 144
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



# function to run n amount of simulations and average the results

def generate_average_plot_of_n_trials(trials: int, population: int) -> None:
    
    '''
        Return:

        creates a plot of the average performance of the precision
        and accuracy of the a confusion matrix over a set number of trials

        (would be nice to add more functionality for simluating the same starting
        matrix for n trials, instead of generating a new random one with each trial)


        Issues:

        Will provide a Runtime warning when the number of trials exceeds 100
        Issue is reported within calculate_accuracy_and_precision()
        
        Still investigating...

        Also will not execute properly when trials = 1, need a case to handle that condition
        ... added single trial case

    '''

    initial_result = generate_performance_metrics_for_all_values_of_prevalence(population)

    prevalence = initial_result['prevalence']

    precision = initial_result['precision']
    accuracy = initial_result['accuracy']

    if trials == 1:

        plt.plot(prevalence, precision, prevalence, accuracy)
        plt.title(f'Performance of 1 trial')
        plt.legend(['Precision', 'Accuracy'])
        plt.xlabel('Prevalence')
        plt.ylabel('Metric (%)')
        plt.show()

        return

    
    n = 1

    while n < trials:
        
        trial_result = generate_performance_metrics_for_all_values_of_prevalence(population)

        # if not ave_precision.shape[0]:
        #     ave_precision = np.append(ave_precision, trial_result['precision'])

        # if not ave_accuracy.shape[0]:
        #     ave_accuracy = np.append(ave_accuracy, trial_result['accuracy'])

        precision = np.vstack([precision, trial_result['precision']])
        accuracy = np.vstack([accuracy, trial_result['accuracy']])
        prevalence = np.vstack([prevalence, trial_result['prevalence']])

        n += 1
    

    # print(precision.shape)  # shape is correct

    # flatten array into one vector of all column averages

    ave_precision = precision.mean(axis=0)
    ave_accuracy = accuracy.mean(axis=0)
    ave_prevalence = prevalence.mean(axis=0)

    plt.plot(ave_prevalence, ave_precision, ave_prevalence, ave_accuracy)
    plt.title(f'Average Performance over {trials} trials')
    plt.legend(['Precision', 'Accuracy'])
    plt.xlabel('Prevalence')
    plt.ylabel('Metric (%)')
    plt.show()

    return



# old function from a previous commit that I haven't deleted, N/A

def old() -> None:

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



# Procedural function to initialize the simulation of the confusion matrix performance

def main() -> None:

    print('\nEnter positive integer values, or press <Ctrl+C> to quit:\n')

    try:

        trials: int     = int(input('\nEnter the number of trials to simulate:\t'))
        population: int = int(input('\nEnter sample population size:\t'))

        generate_average_plot_of_n_trials(trials=trials, population=population)

    except KeyboardInterrupt:

        print('\n\n<Ctrl+C> detected, user elected to quit program. Goodbye :)')

    else:

        print('\nProcessed ended gracefully')



main()
