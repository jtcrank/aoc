with open('input.txt') as f: depths = [int(i) for i in f.readlines()]
increases = [ 1 for i,d in enumerate(depths) if (i > 0) and (d > depths[i-1])]

print(f'Total Increases: {len(increases)}')

