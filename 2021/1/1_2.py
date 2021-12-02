with open('input.txt') as f: depths = [int(i) for i in f.readlines()]

depth_windows = [ sum(depths[i-2:i+1]) for i,d in enumerate(depths) if i > 1 ]
increases = [ '+' for i,d in enumerate(depth_windows) if (i > 0) and (d > depth_windows[i-1]) ]

print(f'Total Increases: {len(increases)}')
