location = [0,0]
aim = 0

class Submarine(object):
    def __init__(self):
        self.location = [0,0]
        self.aim = 0

    def move(self, direction, distance):
        if direction == 'forward':
            self.location[0] += int(distance)
            self.location[1] += (self.aim*int(distance))

        if direction == 'down':
            self.aim += int(distance)

        if direction == 'up':
            self.aim -= int(distance)


with open('input.txt') as f:
    movements = [ i for i in f.readlines() ]

submarine = Submarine()

for movement in movements:
    submarine.move(*movement.split(' '))

print(f'Location: {submarine.location} ({submarine.location[0]*submarine.location[1]})')
