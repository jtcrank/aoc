def get_steps(location, set_1, set_2):
    return set_1[location] + set_2[location]

def walk_path(path):
    locations = {}
    x,y,n = 0,0,0
    for i in path:
        direction = i[:1]
        num_moves = int(i[1:])
        for move in range(0, num_moves):
            if direction == 'U':
                y = y + 1
            if direction == 'D':
                y = y - 1
            if direction == 'R':
                x = x + 1
            if direction == 'L':
                x = x - 1
            n = n + 1
            key = f'{x}x{y}'
            if key not in locations:
                locations[key] = n

    return locations

with open('input.txt') as f:
    paths = f.read().splitlines()

w1_path = paths[0].split(',')
w2_path = paths[1].split(',')

w1_locations = walk_path(w1_path)
w2_locations = walk_path(w2_path)

intersections = [i for i in list(set(w1_locations.keys()).intersection(set(w2_locations.keys())))]
steps = [get_steps(i, w1_locations, w2_locations) for i in intersections]

print(min(steps))
