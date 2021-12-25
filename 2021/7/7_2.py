import math

with open('input.txt') as f:
    positions = sorted([ int(i) for i in f.read().strip().split(',') ])

def calculate_fuel(ideal_pos):
    distances = (abs(ideal_pos - pos) for pos in positions)
    fuel_usages = (int(d * (d + 1) / 2) for d in distances)
    return sum(fuel_usages)


num_positions = len(positions)
mean = ((sum(positions) - len(positions)) / (len(positions) - 1))


upper = math.ceil(mean)
lower = math.floor(mean)

upper_fuel = calculate_fuel(upper)
lower_fuel = calculate_fuel(lower)

if upper_fuel < lower_fuel:
    print(f'Position {upper}: {upper_fuel} fuel')
else:
    print(f'Position {lower}: {lower_fuel} fuel')

