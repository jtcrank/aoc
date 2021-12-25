with open('test_input.txt') as f:
    positions = sorted([ int(i) for i in f.read().strip().split(',') ])

num_positions = len(positions)
median = positions[num_positions//2]

fuel_used = sum(abs(pos-median) for pos in positions)
print(f'Position {median}: {fuel_used} fuel')
