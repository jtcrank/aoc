###################################
# Read input values from txt file #
###################################

with open("input.txt", "r") as input_file:
    raw_values = input_file.read().strip().split("\n")

list_1, list_2 = ([], [])

for line in raw_values:
    vals = line.split()
    list_1.append(int(vals[0]))
    list_2.append(int(vals[1]))

list_1.sort()
list_2.sort()

similarity_score = sum(item * list_2.count(item) for item in list_1)

print(similarity_score)
