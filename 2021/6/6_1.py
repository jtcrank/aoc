class School(object):
    def __init__(self, initial_state):
        self.fish = [ LanternFish(spawn_timer=fish) for fish in initial_state ]


    def grow(self):
        new_members = []
        for f in self.fish:
            new_fish = f.spawn()
            if new_fish: new_members.append(new_fish)

        self.fish.extend(new_members)


    def state(self):
       return [ str(f.spawn_timer) for f in self.fish ]


class LanternFish(object):
    def __init__(self, spawn_timer=8):
        self.spawn_timer = spawn_timer

    def spawn(self):
        if self.spawn_timer == 0:
            self.spawn_timer = 6
            return LanternFish()
        else:
            self.spawn_timer -= 1


with open('input.txt') as f:
    initial_state = [ int(i) for i in f.read().strip().split(',') ]

school = School(initial_state)

for i in range(0,80):
    school.grow()

print(f'Total Fish: {len(school.fish)}')

