import re
from functools import reduce


###################################
# Read input values from txt file #
###################################

input_file = open("input.txt", "r")

input_data = input_file.readlines()
input_file.close()

############
# Solution #
############

total_power = 0

for game in input_data:
    maximums = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    game_id, game_details = re.match(r"Game ([0-9]+): (.+)", game).groups()
    grabs = game_details.split(";")

    for grab in grabs:
        for grab_group in re.findall(r"(([0-9]+)\s(blue|red|green))", grab):
            if maximums[grab_group[2]] < int(grab_group[1]):
                maximums[grab_group[2]] = int(grab_group[1])

    total_power += reduce(lambda x, y: x*y, maximums.values())


print(total_power)
