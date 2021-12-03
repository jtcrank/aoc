with open('input.txt') as f:
    diagnostics = [ [int(i) for i in list(line)] for line in f.read().splitlines() ]

gamma, epsilon = [ int(''.join(b), 2) for b in zip(*[ (['1','0'] if i.count(1) >= i.count(0) else ['0','1']) for i in zip(*diagnostics) ]) ]

print(f'Power Consumption: {gamma * epsilon} (gamma-{gamma} | epsilon-{epsilon})')

