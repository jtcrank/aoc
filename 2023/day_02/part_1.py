import re


###################################
# Read input values from txt file #
###################################

input_file = open("input.txt", "r")

input_data = input_file.readlines()
input_file.close()

############
# Solution #
############

CUBE_COUNTS = {
    "red": 12,
    "blue": 14,
    "green": 13,
}

id_total = 0


def validate_grabs(grabs):
    for grab in grabs:
        for grab_group in re.findall(r"(([0-9]+)\s(blue|red|green))", grab):
            if CUBE_COUNTS[grab_group[2]] < int(grab_group[1]):
                return False

    return True


for game in input_data:
    game_id, game_details = re.match(r"Game ([0-9]+): (.+)", game).groups()
    grabs = game_details.split(";")
    if validate_grabs(grabs):
        id_total += int(game_id)

print(id_total)
