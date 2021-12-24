from collections import defaultdict


# read in vent lines
with open('test_input.txt') as f:
    lines = [ line.split(' -> ') for line in f.read().splitlines() ]


# get all points between endpoints
def draw_line(x1, y1, x2, y2):
    x1, y1, x2, y2 = [ int(i) for i in [x1, y1, x2, y2 ] ]
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    x_coords = [ i for i in range(x1, x2 + 1) ]
    y_step = 1 if y1 <= y2 else -1
    y_coords = [ i for i in range(y1, y2 + y_step, y_step) ]

    x_coords = x_coords * len(y_coords) if len(x_coords) < len(y_coords) else x_coords
    y_coords = y_coords * len(x_coords) if len(y_coords) < len(x_coords) else y_coords

    return [
        f'{coord[0]},{coord[1]}'
        for coord
        in list(zip(list(x_coords), list(y_coords)))
    ]



# draw all lines between vent line endpoints
vents = []
for line in lines:
    vent_line = draw_line(*line[0].split(','), *line[1].split(','))
    if vent_line: vents.extend(vent_line)


# count duplicate points which indicate intersection
point_counts = defaultdict(int)
for vent in vents:
    point_counts[vent] += 1

num_intersections = len([ 1 for point, count in point_counts.items() if count > 1 ])

print(f'Number of vent line intersections: {num_intersections}')
