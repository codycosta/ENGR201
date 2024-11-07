
# dominant and recessive gene simulation with user inputs


# define gene list
dominant = ['cleft chin', 'widow\'s peak', 'dimples', 'brown/black hair', 'freckles', 'brown eyes', 'free earlobe']
recessive = ['no cleft', 'no widow\'s peak', 'no dimples', 'blonde hair', 'no freckles', 'gray/blue eyes', 'attached earlobe']


# ask user how to proceed with the program and validate response
method = None
while method != 'for' and method != 'while':
    method = input('how shall we proceed? Enter [for | while] to pick a looping scheme:\t')


# using primary for loop
if method == 'for':

    repetitions = None
    while repetitions not in ['1', '2', '3', '4', '5', '6', '7', '8', '9' , '10']:

        repetitions = input('how many times would you like to run the program?\t')
    
    for j in range(int(repetitions)):
    
        # validate user inputs

        match = None
        while not match:
            print('\n////////////////////////////////////////////////////////////////////////////////////////////////')
            print('\nPlease choose a set of genes, one equally dominant and recessive (ex. cleft chin & no cleft)\n')
            print('////////////////////////////////////////////////////////////////////////////////////////////////\n')

            gene_1 = input('Enter the first gene:\t')
            gene_2 = input('Enter the second gene:\t')


            while gene_1 not in dominant and gene_1 not in recessive:
                gene_1 = input('First selected gene not found in either dominant or recessive lists, please enter again:\t')
                

            while gene_2 not in dominant and gene_2 not in recessive:
                gene_2 = input('Second selected gene not found in either dominant or recessive lists, please enter again:\t')

            print(f'\ngene 1 = {gene_1},\t gene 2 = {gene_2}')


            # inputs validated to each list, now we need to match them based on list index

            if dominant.index(gene_1) == recessive.index(gene_2) or dominant.index(gene_2) == recessive.index(gene_1):
                print('match found!')
                match = True

            else:
                print('\nno match found, please select a dominant/recessive pair of genes\n')
                match = False


        if gene_1 in dominant:
            print(f'\nDominant gene = {gene_1}')
        else:
            print(f'\nDominant gene = {gene_2}')


        if repetitions > 1:
            proceed = None
            while proceed not in ['y', 'yes', 'n', 'no']:
                proceed = input('would you like to continue? [y | yes | n | no]:\t')
                
            if proceed == 'n' or proceed == 'no':
                print('Program exited early by user')
                break



# using primary while loop
elif method == 'while':

    repetitions = None
    while repetitions not in ['1', '2', '3', '4', '5', '6', '7', '8', '9' , '10']:

        repetitions = input('how many times would you like to run the program?\t')

    j = 0

    while j < int(repetitions):
    
        # validate user inputs

        match = None
        while not match:
            print('\n////////////////////////////////////////////////////////////////////////////////////////////////')
            print('\nPlease choose a set of genes, one equally dominant and recessive (ex. cleft chin & no cleft)\n')
            print('////////////////////////////////////////////////////////////////////////////////////////////////\n')

            gene_1 = input('Enter the first gene:\t')
            gene_2 = input('Enter the second gene:\t')


            while gene_1 not in dominant and gene_1 not in recessive:
                gene_1 = input('First selected gene not found in either dominant or recessive lists, please enter again:\t')
                

            while gene_2 not in dominant and gene_2 not in recessive:
                gene_2 = input('Second selected gene not found in either dominant or recessive lists, please enter again:\t')

            print(f'\ngene 1 = {gene_1},\t gene 2 = {gene_2}')


            # inputs validated to each list, now we need to match them based on list index

            if dominant.index(gene_1) == recessive.index(gene_2) or dominant.index(gene_2) == recessive.index(gene_1):
                print('match found!')
                match = True

            else:
                print('\nno match found, please select a dominant/recessive pair of genes\n')
                match = False

        
        if gene_1 in dominant:
            print(f'\nDominant gene = {gene_1}')
        else:
            print(f'\nDominant gene = {gene_2}')


        if repetitions > 1:
            proceed = None
            while proceed not in ['y', 'yes', 'n', 'no']:
                proceed = input('would you like to continue? [y | yes | n | no]:\t')
                
            if proceed == 'n' or proceed == 'no':
                print('Program exited early by user')
                break

        j += 1
    