import re


###################################
# Read input values from txt file #
###################################

with open('input.txt', 'r') as input_file:
    corrupted_memory = input_file.read().strip().replace('\n', '')

mul_pattern = r"mul\((\d{1,3},\d{1,3})\)"

mul_instructions = re.findall(mul_pattern, corrupted_memory)

result = sum(
    a * b
    for a, b
    in [
        map(int, mul.split(','))
        for mul
        in
        mul_instructions
    ]
)

print(result)
