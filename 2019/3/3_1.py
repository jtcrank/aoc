def manhattan_distance(a, b):
    return abs(a) + abs(b)

def walk_path(path):
    locations = []
    x,y = 0,0
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
            locations.append(f'{x}:{y}')

    return locations

with open('input.txt') as f:
    paths = f.read().splitlines()

w1_path = paths[0].split(',')
w2_path = paths[1].split(',')

w1_locations = walk_path(w1_path)
w2_locations = walk_path(w2_path)

intersections = [i.split(':') for i in list(set(w1_locations).intersection(set(w2_locations)))]
distances = [manhattan_distance(int(i[0]), int(i[1])) for i in intersections]

print(min(distances))
