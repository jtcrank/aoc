import re
from collections import defaultdict

###################################
# Read input values from txt file #
###################################

input_file = open("input.txt", "r")

schematic = input_file.read().splitlines()
input_file.close()


############
# Solution #
############

schematic_line_count = len(schematic)
schematic_line_length = len(schematic[0])


def process_number(
    number,
    possible_gears,
    line_num,
    num_start,
    num_end
):
    # generate a list of coordinates in which to check for a possible gear
    # ignoring coordinates that would fall outside of the bounds of
    # line count and line length.
    checkpoints = [
        [x, y]
        for x in range(num_start - 1, num_end + 1)
        for y in range(line_num - 1, line_num + 2)
        if (
            (x >= 0 and x <= schematic_line_length - 1)
            and
            (y >= 0 and y <= schematic_line_count - 1)
        )
    ]

    for checkpoint in checkpoints:
        # Check if the character at coordinates is a possible gear
        # and track for futher processing
        char = schematic[checkpoint[1]][checkpoint[0]]
        if re.match(r"\*", char):
            possible_gears[f"{checkpoint[1]},{checkpoint[0]}"].append(int(number))


# List of possible gears and connected parts
possible_gears = defaultdict(list)

for line_num, schematic_line in enumerate(schematic):
    is_part_num = False

    number_matches = re.finditer(r"\d+", schematic_line)

    for m in number_matches:
        process_number(m[0], possible_gears, line_num, m.start(0), m.end(0))

total_gear_ratio = sum(
    parts[0] * parts[1]
    for _, parts
    in possible_gears.items()
    if len(parts) == 2
)

print(total_gear_ratio)
