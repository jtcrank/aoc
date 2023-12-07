import re
from collections import defaultdict


###################################
# Read input values from txt file #
###################################

input_file = open("input.txt", "r")

cards = input_file.read().splitlines()
input_file.close()


############
# Solution #
############

card_tracker = defaultdict(lambda: 0)

for idx, card in enumerate(cards):
    # include original card in tracker
    card_tracker[idx] += 1

    win, have = re.match(r"Card\s+\d+:\s*([\d\s]+)\s+\|\s+([\d\s]+)", card).groups()
    winning_matches = list(set(win.split()) & set(have.split()))
    for idx_2, _ in enumerate(winning_matches):
        card_number = idx + idx_2 + 1
        if not card_number >= len(cards):
            # Add an amount of copies of below cards
            # equal to the number of copies of current card
            card_tracker[card_number] += 1 * card_tracker[idx]

print(sum(card_tracker.values()))
