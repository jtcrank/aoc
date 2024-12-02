###################################
# Read input values from txt file #
###################################

with open("input.txt", "r") as input_file:
    raw_values = input_file.read().strip().split("\n")

reports = [ line.split() for line in raw_values ]

def is_safe_report(report):
    result = True

    prev_delta = None

    for i in range(len(report) - 1):
        delta = int(report[i+1]) - int(report[i])

        if (
            (abs(delta) < 1 or abs(delta) > 3)
            or
            (prev_delta and prev_delta * delta <= 0)
        ):
            return False

        prev_delta = delta

    return result

results = [ is_safe_report(report) for report in reports ]

safe_report_count = sum(1 for result in results if result)

print(safe_report_count)
