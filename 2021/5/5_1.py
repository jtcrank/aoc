from collections import defaultdict


# read in vent lines
with open('input.txt') as f:
    lines = [ line.split(' -> ') for line in f.read().splitlines() ]


# get all points between endpoints
def draw_line(x1, y1, x2, y2):
    x1, y1, x2, y2 = [ int(i) for i in [x1, y1, x2, y2 ] ]

    if x1 == x2:
        return [ f'{x1},{i}' for i in range(min(y1,y2), max(y1,y2) + 1) ]
    elif y1 == y2:
        return [ f'{i},{y1}' for i in range(min(x1,x2), max(x1,x2) + 1) ]
    else:
        None


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
