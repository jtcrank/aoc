###################################
# Read input values from txt file #
###################################

with open("input.txt", "r") as input_file:
    raw_values = input_file.read().strip().split("\n")

def is_safe_report(report):
    prev_delta = None

    for a, b in zip(report, report[1:]):
        delta = int(b) - int(a)

        if abs(delta) not in {1, 2, 3} or (prev_delta and prev_delta * delta <= 0):
            return False

        prev_delta = delta

    return True


# Process the data
reports = [list(map(int, line.split())) for line in raw_values]
safe_report_count = sum(is_safe_report(report) for report in reports)

print(safe_report_count)

