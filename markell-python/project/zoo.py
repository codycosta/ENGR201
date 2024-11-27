'''
Zoo Project Layout:

Example structure given was to log the times of day the animals get fed, what type of food they eat, medical conditions, etc.


Required code usage:

1.  multi line comment                                      done
2.  1 or more constants                                     done
3.  3 or more user defined functions                        done
4.  1 or more loops (for or while, doesn't matter)          done
5.  1 or more conditional blocks (if, elif, else)           done
6.  use of file handling                                    done
7.  Dictionary OR                                           done
    List/Tuple(+5 or more manipulations) OR 
    Set(+5 or more manipulations)


Data Structuring Example:

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

'''

from helper_functions import *


# Define the size of our zoo animal population
POPULATION = None
while POPULATION not in [f'{x}' for x in range(1, 51)]:
    POPULATION = input('Enter zoo population size [1 - 50]:\t')
POPULATION = int(POPULATION)


# Let's start by creating a list of what animals should be included within our zoo :)
zoo_animals_species = ['bear', 'lion', 'tiger', 'snake', 'zebra', 'giraffe', 'hippo', 'lizard', 'fish', 'panda', 'goat', 'camel', 'tortoise', 'sea turtle', 'whale', 'panther', 'elephant', 'rhino', 'flamingo', 'monkey', 'owl']


# We can also create some subclasses of food preference of each animal
diet = ['carnivore', 'herbivore', 'omnivore']
carnivorous_foods = ['veal', 'chicken', 'fish']
herbivorous_foods = ['plants', 'leaves', 'grass']


# Now we need a list of animal names (sourced in animal-names.txt file created from https://www.bluecross.org.uk/sites/default/files/d8/downloads/Blue-Cross-top-100-pet-dog-names.pdf)
common_animal_names = None
with open('animal-names.txt', 'r') as file:
    common_animal_names = file.readline().split(' ')


# generate a list of common animal health conditions, favoring healthy (health-condition.txt file created from https://www.ardmoreah.com/resources/pet-care/common-pet-health-issues/)
animal_health_conditions = None
with open('health-conditions.txt', 'r') as file:
    animal_health_conditions = file.readline().split(',')
for k in range(20):
    animal_health_conditions.append('healthy')


# generate a list of possible animal personalities
animal_personalities = None
with open('personalities.txt', 'r') as file:
    animal_personalities = file.readline().split(' ')


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
