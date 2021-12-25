class School(object):
    def __init__(self, initial_state):
        self.fish = []
        self.babies = [0,0]
        for i in range(0,7):
            self.fish.append(initial_state.count(i))

    def grow(self):
        spawn_count = self.fish.pop(0)
        newly_matured = self.babies.pop(0)
        self.fish.append(spawn_count + newly_matured)
        self.babies.append(spawn_count)


    def population(self):
        return sum([*self.fish, *self.babies])



with open('input.txt') as f:
    initial_state = [ int(i) for i in f.read().strip().split(',') ]

school = School(initial_state)

for i in range(0,256):
    school.grow()

print(f'Total Fish: {school.population()}')

