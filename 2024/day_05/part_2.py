import re


###################################
# Read input values from txt file #
###################################

with open("input.txt", "r") as input_file:
    data = input_file.read()
    rules, updates = (
        [
            list(map(int, re.split(r'\||,', item)))
            for item
            in datum.strip().split('\n')
        ]
        for datum
        in data.split('\n\n')
    )

sum_of_fixed_mids = 0

for pages in updates:
    applicable_rules = []
    is_valid = True

    weights = {
        page: 0
        for page
        in pages
    }

    for rule in rules:
        if set(rule).issubset(pages):
            weights[rule[0]] += 1
            applicable_rules.append(rule)
            if is_valid:
                is_valid = pages.index(rule[0]) < pages.index(rule[1])

    if not is_valid:
        for page, weight in weights.items():
            if weight == int((len(pages) - 1) / 2):
                sum_of_fixed_mids += page

print(sum_of_fixed_mids)
