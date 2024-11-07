# void function, nothing returnes
def ask_to_proceed():
    proceed = None
    while proceed not in ['y', 'yes', 'n', 'no']:
        proceed = input('would you like to continue? [y | yes | n | no]:\t')
        
    if proceed in ['n', 'no']:
        print('Program exited early by user')
        raise SystemExit


# value returning functions
def decide_repetitions():
    reps = None
    while reps not in ['1', '2', '3', '4', '5', '6', '7', '8', '9' , '10']:
        reps = input('How many times should the program run?:\t')
    
    return int(reps)


def decide_control_flow():
    method = None
    while method not in ['for', 'while']:
        method = input('how shall we proceed? Enter [for | while] to pick a looping scheme:\t')
    
    return method


# pass an argument to a function / local variable functions
def validate_inputs_and_find_match(gene_1, gene_2, dominant, recessive):

    # print('\n////////////////////////////////////////////////////////////////////////////////////////////////')
    # print('\nPlease choose a set of genes, one equally dominant and recessive (ex. cleft chin & no cleft)\n')
    # print('////////////////////////////////////////////////////////////////////////////////////////////////\n')

    # gene_1 = input('Enter the first gene:\t')
    # gene_2 = input('Enter the second gene:\t')

    while gene_1 not in dominant and gene_1 not in recessive:
        gene_1 = input('First selected gene not found, try again:\t')

    while gene_2 not in dominant and gene_2 not in recessive:
        gene_2 = input('Second selected gene not found, try again:\t')

    # check for gene match
    # if dominant.index(gene_1) == recessive.index(gene_2) or dominant.index(gene_2) == recessive.index(gene_1):
    try:
        if dominant.index(gene_1) == recessive.index(gene_2):
            print('match found!')
            match = True
    
    except ValueError:
        if dominant.index(gene_2) == recessive.index(gene_1):
            print('match found!')
            match = True
        
    if not match:
        print('\nno match found, please select a dominant/recessive pair of genes\n')
        match = False

    return match


def print_dominant_gene(gene_1, gene_2, dominant):
    if gene_1 in dominant:
        print(f'\nDominant gene = {gene_1}\n')
    elif gene_2 in dominant:
        print(f'\nDominant gene = {gene_2}\n')


# another void function with no defined return value
def main_procedure(dominant, recessive):
    match: bool = False
    while not match:
        print('\n////////////////////////////////////////////////////////////////////////////////////////////////')
        print('\nPlease choose a set of genes, one equally dominant and recessive (ex. cleft chin & no cleft)\n')
        print('////////////////////////////////////////////////////////////////////////////////////////////////\n')

        gene_1 = input('Enter the first gene:\t')
        gene_2 = input('Enter the second gene:\t')

        match = validate_inputs_and_find_match(gene_1, gene_2, dominant, recessive)
        print_dominant_gene(gene_1, gene_2, dominant)

