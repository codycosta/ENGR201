'''
Zoo Project Layout:
///////////////////

Example structure given was to log the times of day the animals get fed, what type of food they eat, medical conditions, etc.
We will use this and build upon it!


Required Code Usage:
////////////////////

1.  multi line comment                                      done
2.  1 or more constants                                     done
3.  3 or more user defined functions                        done
4.  1 or more loops (for or while, doesn't matter)          done
5.  1 or more conditional blocks (if, elif, else)           done
6.  use of file handling                                    done
7.  Dictionary OR                                           done
    List/Tuple(+5 or more manipulations) OR 
    Set(+5 or more manipulations)


Zoo Data Structure:
///////////////////

Zoo_data = {

    'Animals': {
        'name': {
            species: _, 
            age: _, 
            personality: _,
            diet: _
        }
    },

    
    '7-Day Feeding Logs': {
        'name': {
            breakfasts: {times/dates: food eaten}, 
            lunches: {times/dates: food eaten}, 
            dinners: {times/dates: food eaten}
        }
    },

    
    'Medical Conditions': {
        'name': 'medical state'
    }

}


Program Description:
////////////////////

Overview:
Zoo.py is the main program in a set of 2 files that manages the data of our zoo; this includes information such as animal species, age, diet preference, personality, and the cute names given to them.

How it works:
The program will ask the user to input a positive integer value between 1 and 50 to represent the number of animals housed within our zoo. Some error checking is implemented to ensure we get a valid response.
A few setup variables are initialized to consist of the variety of animal species present in the zoo, as well as the diets and food groups thereof, for each animal.
To supplement our zoo with some real life data, a few text files were created prior to the scripting of this program to serve as reference data for the animal names, personalities, and common health conditions.
Zoo.py will read from each of these files to pull said data into lists to be used later.
The data pulled from the text files is then passed to the helper_functions.py script's generate_zoo_population() function to randomize some combinations of data to represent each animal, using each name only once.
Similar procedures are used for generate_health_data() and generate_feeding_logs() where health issues are randomly assigned to each animal (with a strong bias for a healthy medical state) and feed logs are generated
based on the random assignment of diet preference and include 3 meals a day for the most recent 7 day period (in real time) with their own timestamps.
The output data of the 3 mentioned helper functions are each saved to their own dictionary (see data structure above for the final result) for easy access and uniqueness.
Once all of the data has been placed into their own dict and then packed into a wrapper dict named 'Zoo_data{}' the resulting data structure is passed to the final helper function: display_zoo_data().
This function processes the main dict structure and prints its contents in a more readable fashion than the default interpreted printout.
Out.txt will serve as the generated terminal history record once the program finishes execution

'''

from helper_functions import *

print('out.txt\n')


# Define the size of our zoo animal population
POPULATION = None
while POPULATION not in [f'{x}' for x in range(1, 51)]:
    POPULATION = input('Enter zoo population size [1 - 50]:\t')
POPULATION = int(POPULATION)
print(f'\nGenerating zoo with animal population of {POPULATION}')
print('*' * 30 + '\n')


# Let's start by creating a list of what animals should be included within our zoo :)
zoo_animals_species = ['bear', 'lion', 'tiger', 'snake', 'zebra', 'giraffe', 'hippo', 'lizard', 'fish', 'panda', 'goat', 'camel', 'tortoise', 'sea turtle', 'whale', 'panther', 'elephant', 'rhino', 'flamingo', 'monkey', 'owl']


# We can also create some subclasses of food preference of each animal
diet = ['carnivore', 'herbivore', 'omnivore']
carnivorous_foods = ['veal', 'chicken', 'fish']
herbivorous_foods = ['plants', 'leaves', 'grass']


# Now we need a list of animal names (sourced in animal-names.txt file created from https://www.bluecross.org.uk/sites/default/files/d8/downloads/Blue-Cross-top-100-pet-dog-names.pdf)
with open('animal-names.txt', 'r') as file:
    common_animal_names = file.readline().split(' ')
print(f'List of common animal names within animal-names.txt:\n{common_animal_names}\n')


# generate a list of common animal health conditions, favoring healthy (health-condition.txt file created from https://www.ardmoreah.com/resources/pet-care/common-pet-health-issues/)
with open('health-conditions.txt', 'r') as file:
    animal_health_conditions = file.readline().split(',')
for k in range(20):
    animal_health_conditions.append('healthy')
print(f'List of common medical issues within health-conditions.txt:\n{animal_health_conditions}\n')


# generate a list of possible animal personalities
with open('personalities.txt', 'r') as file:
    animal_personalities = file.readline().split(' ')
print(f'List of common animal personalities within personalities.txt:\n{animal_personalities}\n')


# Randomize some pairs of animals and names to create unique, non repeating entries for our database dictionary
Animals = generate_zoo_population(POPULATION, zoo_animals_species, common_animal_names, animal_personalities, diet)
# print(f'\nAnimal Info:\n{Animals}\n\n')


# create a new dict to store the health conditions of each animal
Health_data = generate_health_data(Animals, animal_health_conditions)
# print(f'Animal Health:\n{Health_data}\n\n')


# create another new dict to hold data of the 7 day feeding log
Feed_data = generate_feeding_logs(Animals, carnivorous_foods, herbivorous_foods)
# print(f'Animal Feed:\n{Feed_data}\n\n')


# clump all data together like so, not really sure why we need this but oh well
Zoo_data = {
    'Animals': Animals,
    '7-Day Feed Log': Feed_data,
    'Health Status': Health_data
}


# Print data in clean, easy to read fashion
display_zoo_data(Zoo_data)
