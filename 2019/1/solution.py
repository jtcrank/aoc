import os
import math

with open('input.txt') as f:
    masses = f.read().splitlines()

fuel_required = sum([(math.floor(int(m) / 3) - 2) for m in masses])
print(fuel_required)

