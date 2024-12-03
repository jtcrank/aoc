import re


###################################
# Read input values from txt file #
###################################

with open('input.txt', 'r') as input_file:
    corrupted_memory = input_file.read().strip().replace('\n', '')

# Regex
mem_segment_rgx = r"(do|don't)\(\)"
mul_rgx = r"mul\((\d{1,3},\d{1,3})\)"

mem_segments = re.split(mem_segment_rgx, corrupted_memory)

result = 0
current_directive = "do"
for mem_segment in mem_segments:
    if mem_segment in ["do", "don't"]:
        current_directive = mem_segment
        continue

    if current_directive == "don't":
        continue
    else:
        mul_instructions = re.findall(mul_rgx, mem_segment)
        result += sum(
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
