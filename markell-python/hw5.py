import math
import json
import csv


# *****************************************************************************************************************
# Part 1:   OOP, machine class definitions
# *****************************************************************************************************************
class Beam:
    # properties
    def __init__(self, mass, length, width, height):
        self.mass = mass
        self.length = length
        self.width = width
        self.height = height

    # methods
    def calc_mass_moment_of_inertia(self):
        # approximation if beam is modeled as a rod
        return 1/12 * self.mass * self.length**2
    
    def calc_center_of_mass(self) -> tuple:
        x = self.width / 2
        y = self.length / 2
        return (x, y)

    def calc_area_moment_of_intertia(self):
        # area of cross section
        return 1/12 * self.width * self.height**3
    
    def get_all_attrs_by_value(self) -> list:
        return [self.mass, self.length, self.width, self.height]

    
class Pulley:
    def __init__(self, radius, wrap_angle, tension, mass):
        self.radius = radius
        self.wrap_angle = wrap_angle
        self.tension = tension
        self.mass = mass

    def calc_mass_moment_of_intertia(self):
        # disk model approximation
        return 1/4 * self.mass * self.radius**2

    def calc_angular_acceleration(self):
        # T = I*a
        return self.tension / self.calc_mass_moment_of_intertia()

    def calc_coefficient_of_friction(self):
        # T = exp(u * angle)    crude approximation for belt friction: T1 = T2 * exp(u * wrap_angle)
        return math.log(self.tension, math.e) / self.wrap_angle
    
    def get_all_attrs_by_value(self) -> list:
        return [self.radius, self.wrap_angle, self.tension, self.mass]


class Wedge:
    def __init__(self, angle, length, height, width):
        self.angle = angle
        self.length = length
        self.height = height
        self.width = width

    def calc_static_friction_coefficient(self):
        return math.tan(self.angle)

    def calc_mechanical_advantage(self):
        # ratio of weight on slope vs vertical weight
        return 1 / math.sin(self.angle)

    def calc_volume(self):
        return 1/2 * self.length * self.width * self.height
    
    def get_all_attrs_by_value(self) -> list:
        return [self.angle, self.length, self.height, self.width]


class Piston:
    def __init__(self, pressure, extension_length, temperature_K, radius, Cp):
        self.pressure = pressure
        self.stroke = extension_length
        self.temperature = temperature_K
        self.radius = radius
        self.specific_heat = Cp

    def calc_volume(self):
        return math.pi * self.radius**2 * self.stroke
    
    def calc_flow_work(self):
        # W = P * V
        return self.pressure * self.calc_volume()
    
    def calc_entropy_change(self):
        return self.Cp * math.log(self.temperature / 293, math.e)
    
    def get_all_attrs_by_value(self) -> list:
        return [self.pressure, self.stroke, self.temperature, self.radius, self.specific_heat]
    
# output print


# *****************************************************************************************************************
# Part 2:   Class Instances using FOR or WHILE loop
# *****************************************************************************************************************
classes = ['Beam', 'Pulley', 'Wedge', 'Piston']
machines = []

for machine in classes:
    # create each machine class
    print(f'\nCreating {machine} class instance:\n')

    if machine == 'Beam':
        mass = float(input('enter a mass:\t\t'))
        length = float(input('enter a length:\t\t'))
        width = float(input('enter a width:\t\t'))
        height = float(input('enter a height:\t\t'))

        beam = Beam(mass, length, width, height)
        machines.append(beam)

    if machine == 'Pulley':
        radius = float(input('enter a radius:\t\t'))
        angle = float(input('enter a wrap angle:\t\t'))
        tension = float(input('enter a tension force:\t\t'))
        mass = float(input('enter a mass:\t\t'))

        pulley = Pulley(radius, angle, tension, mass)
        machines.append(pulley)

    if machine == 'Wedge':
        angle = float(input('enter an angle:\t\t'))
        length = float(input('enter a length:\t\t'))
        height = float(input('enter a height:\t\t'))
        width = float(input('enter a width:\t\t'))

        wedge = Wedge(angle, length, height, width)
        machines.append(wedge)

    if machine == 'Piston':
        pressure = float(input('enter a pressure:\t\t'))
        stroke = float(input('enter a stroke length:\t\t'))
        temperature = float(input('enter a temperature in K:\t\t'))
        radius = float(input('enter a radius:\t\t'))
        cp = float(input('enter specific heat of material:\t\t'))

        piston = Piston(pressure, stroke, temperature, radius, cp)
        machines.append(piston)

# insert 5th item at position 2 in list
machines.insert(1, Piston(100, 4, 2000, 0.5, 4.15))

# print list
print(machines)

# print 2nd - 4th list entries
print(machines[1:4])

# # add another machine to end
machines.append(Wedge(math.pi / 4, 5, 2, 1.5))

# print last entry
print(machines[-1])

# print num machines
print(len(machines))

# print max and min values on list ?
min_max_attrs = []
for machine in machines:
    min_max_attrs.append(min(machine.get_all_attrs_by_value()))
    min_max_attrs.append(max(machine.get_all_attrs_by_value()))

print(min(min_max_attrs))
print(max(min_max_attrs))

# change to a tuple
machines = tuple(machines)
print(machines)


# *****************************************************************************************************************
# Part 3: .txt file writing
# *****************************************************************************************************************
filename = 'device.txt'
with open(filename, 'w') as F:

    for m in machines:
        writestr = f''
        writestr += f'Name: {m}, {vars(m)}\n'

        F.write(writestr)
        print(writestr)

F = open(filename, 'a')

mech7 = Piston(20, 3, 500, 2.1, 4.222)
mech8 = Beam(300, 1, 1.1, 10)

F.write(f'Name: {mech7}, {vars(mech7)}\n')
F.write(f'Name: {mech8}, {vars(mech8)}\n')

F.close()

print(f'Name: {mech7}, {vars(mech7)}\n')
print(f'Name: {mech8}, {vars(mech8)}\n')


# *****************************************************************************************************************
# Part 4: Dictionaries and file writing
# *****************************************************************************************************************
test_takers_birthyear = {
    'License Number': ['F1234567', 'F9876543', 'F0101010'],
    'Birth Year': [2005, 2006, 2007]
}

test_takers_surname = {
    'License Number': ['F1234567', 'F9876543', 'F0101010'],
    'Last Name': ['Smith', 'Doe', 'Costa']
}

test_takers_feespaid = {
    'License Number': ['F1234567', 'F9876543', 'F0101010'],
    'Fee': [100, 150, 200]
}

num_to_search = input('Enter a driver\'s license number:\t')
while num_to_search not in test_takers_birthyear['License Number']:
    num_to_search = input('Submission not found. Enter a valid driver\'s license number:\t')

idx = test_takers_birthyear['License Number'].index(num_to_search)
print(f'\nResults:\tBirth Year: {test_takers_birthyear["Birth Year"][idx]}\tLast name: {test_takers_surname["Last Name"][idx]}\tFee Paid: ${test_takers_feespaid["Fee"][idx]}\n')

# write data to text file
filename = 'test_takers_feespaid.txt'
with open(filename, 'w') as F:
    for key in test_takers_feespaid.keys():
        F.write(f'{key}: {test_takers_feespaid[key]}\n')

# write data to json file
filename_json = 'test_takers_feespaid.json'
with open(filename_json, 'w') as FJ:
    json.dump(test_takers_feespaid, FJ)


# write to csv file
filename_csv = 'test_takers_feespaid.csv'
with open(filename_csv, 'w') as FC:
    writer = csv.DictWriter(FC, test_takers_feespaid.keys())
    writer.writeheader()
    writer.writerow(test_takers_feespaid)


# *****************************************************************************************************************
# Part 5: Sets
# *****************************************************************************************************************
machineset = set(machines[:3])
print(machineset)
print(len(machineset))

color = 'violet'
for char in color:
    machineset.add(char)

print(machineset)

# with exception to letter 'v'
if not 'v' in machineset:
    raise IndexError

else:
    # no exception
    machineset.remove('v')

print(machineset)

