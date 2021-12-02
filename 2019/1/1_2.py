import math

def get_fuel_requirement(mass):
    required_fuel = math.floor(mass / 3) - 2
    if required_fuel <= 0:
        return 0
    else:
        return required_fuel + get_fuel_requirement(required_fuel)

with open('input.txt') as f:
    masses = f.read().splitlines()


fuel_required = sum([get_fuel_requirement(int(m)) for m in masses])
print(fuel_required)

