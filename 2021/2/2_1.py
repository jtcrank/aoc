location = [0,0]

def move(direction, distance):
    if direction == 'forward':
        location[0] += int(distance)

    if direction == 'down':
        location[1] += int(distance)

    if direction == 'up':
        location[1] -= int(distance)

with open('input.txt') as f:
    movements = [ i for i in f.readlines() ]

for movement in movements:
    move(*movement.split(' '))

print(f'Location: {location} ({location[0]*location[1]})')
