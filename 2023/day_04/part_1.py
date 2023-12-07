import re
from functools import reduce


###################################
# Read input values from txt file #
###################################

input_file = open("input.txt", "r")

cards = input_file.read().splitlines()
input_file.close()


############
# Solution #
############

total_points = 0

for card in cards:
    win, have = re.match(r"Card\s+\d+:\s*([\d\s]+)\s+\|\s+([\d\s]+)", card).groups()

    winning_matches = list(set(win.split()) & set(have.split()))
    total_points += reduce(
        lambda total, wn: (total or 1) * (2 if wn[0] else 1),
        enumerate(winning_matches),
        0
    )

print(total_points)
