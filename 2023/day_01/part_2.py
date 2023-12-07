import re


###################################
# Read input values from txt file #
###################################

input_file = open("input.txt", "r")

data = input_file.read()
raw_values = data.strip().split("\n")
input_file.close()

############
# Solution #
############

int_words = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

pattern = r"(?=(" + "|".join(int_words.keys()) + "|[0-9]))"

total_sum = 0

for item in raw_values:
    numeric_matches = re.finditer(pattern, item)
    numeric_values = [
        int(int_words.get(i.group(1), i.group(1)))
        for i
        in numeric_matches
    ]

    total_sum += int(f"{numeric_values[0]}{numeric_values[-1]}")

print(total_sum)
