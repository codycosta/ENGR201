# user defined functions for zoo.py

import random
import datetime

def generate_zoo_population(POPULATION, ANIMALS, NAMES, PERSONALITY, DIET) -> dict:

    Animals = {}

    for k in range(POPULATION):
        # choose random animal as index from list
        animal_idx = random.randint(0, len(ANIMALS)-1)
        species = ANIMALS[animal_idx]

        # choose random name as index from list and remove it from the names array
        name_idx = random.randint(0, len(NAMES)-1)
        name = NAMES[name_idx]
        NAMES.remove(name)

        # choose random personality trait
        personality_idx = random.randint(0, len(PERSONALITY)-1)
        personality = PERSONALITY[personality_idx]

        # choose random diet preference for each animal (results might not make sense in real life but whatever)
        diet_idx = random.randint(0, len(DIET)-1)
        diet = DIET[diet_idx]

        Animals[name] = {
            'species': species,
            'age': random.randint(1, 50),
            'personality': personality,
            'diet': diet
        }

    return Animals


def generate_health_data(animals, HEALTH) -> dict:
    
    health_data = {}
    animal_names = animals.keys()

    for name in animal_names:
        health_data[name] = HEALTH[random.randint(0, len(HEALTH)-1)]
    
    return health_data


def generate_feeding_logs(animals, carnivorous_foods, herbivorous_foods) -> dict:
    # thinking we could generate roughly a week's worth of logs, 3 meals a day, 7 days
    # would incorporate some pseudo random timing such that feeding isnt always the same time each day
    # need also to include the food each animal eats

    feeding_data = {}
    animal_names = animals.keys()

    breakfast_hours = [6, 7, 8, 9]
    lunch_hours = [12, 13, 14, 15]
    dinner_hours = [19, 20, 21, 22]

    month = datetime.datetime.now().month
    end_day = datetime.datetime.now().day
    year = datetime.datetime.now().year

    feeding_dates = []

    for k in range(8):

        # k should increment from 0 to 7
        day = end_day - k

        if day == 0:
            month -= 1

            if month in [9, 4, 6, 11]:
                day = 30
            elif month == 2 and year % 4 == 0:
                day = 29
            elif month == 2:
                day = 28
            else:
                day = 31

        feeding_dates.append(f'{year}/{month}/{day}')   # working as expected so far

    feeding_dates.reverse()

    for name in animal_names:
        # need to generate the most recent week of feeding
        # lets end with today's date for fun :)

        diet = animals[name]['diet']
        food_choices = None
        
        breakfasts = {}
        lunches = {}
        dinners = {}

        for day in feeding_dates:
            rand_minute = random.randint(0, 59)
            if rand_minute < 10:
                rand_minute = f'0{rand_minute}'

            if diet == 'carnivore':
                food_choices = carnivorous_foods
            elif diet == 'herbivorous':
                food_choices = herbivorous_foods
            else:
                food_choices = carnivorous_foods + herbivorous_foods


            breakfasts[f'{day}-{breakfast_hours[random.randint(0, 3)]}:{rand_minute}'] = food_choices[random.randint(0, len(food_choices)-1)]
            lunches[f'{day}-{lunch_hours[random.randint(0, 3)]}:{rand_minute}'] = food_choices[random.randint(0, len(food_choices)-1)]
            dinners[f'{day}-{dinner_hours[random.randint(0, 3)]}:{rand_minute}'] = food_choices[random.randint(0, len(food_choices)-1)]

        feeding_data[name] = {
            'breakfasts': breakfasts,
            'lunches': lunches,
            'dinners': dinners
        }

    return feeding_data


def display_zoo_data(ZOO):

    # get ZOO dict keys
    for key in ZOO.keys():

        match key:
            case 'Animals':
                print('\nAnimal Info')
                print('*' * 30)
                for name in ZOO[key].keys():
                    data = ZOO[key][name]
                    print(f'{name}: {data['species']}, {data['age']} years, {data['personality']}, {data['diet']}\n')

            case '7-Day Feed Log':
                print('7-Day Feed Log')
                print('*' * 30)
                for name in ZOO[key].keys():
                    data = ZOO[key][name]
                    print(f'{name}:\nbreakfasts: {data['breakfasts']}\nlunches: {data['lunches']}\ndinners: {data['dinners']}\n')

            case 'Health Status':
                print('Animal Health Status')
                print('*' * 30)
                for name in ZOO[key].keys():        
                    print(f'{name}:\t{ZOO[key][name]}')

    print()
