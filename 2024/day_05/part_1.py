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


sum_of_valid_mids = sum(
    pages[int((len(pages) - 1) / 2)]
    for pages
    in updates
    if all([
        pages.index(rule[0]) < pages.index(rule[1])
        for rule
        in rules
        if set(rule).issubset(pages)
    ])
)

print(sum_of_valid_mids)
