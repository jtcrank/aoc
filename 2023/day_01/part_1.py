###################################
# Read input values from txt file #
###################################

input_file = open("input.txt", "r")

raw_values = input_file.read().split_lines()
input_file.close()


############
# Solution #
############

calibration_values = []

for item in raw_values:
    numeric_values = [i for i in item if i.isnumeric()]
    if len(numeric_values) > 1:
        cal_val = int(f"{numeric_values[0]}{numeric_values[-1]}")
    else:
        cal_val = int(f"{numeric_values[0]}{numeric_values[0]}")

    calibration_values.append(cal_val)

print(sum(calibration_values))
