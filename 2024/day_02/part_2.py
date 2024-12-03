###################################
# Read input values from txt file #
###################################

with open("input.txt", "r") as input_file:
    raw_values = input_file.read().strip().split("\n")


def evaluate_report(report):
    prev_delta = None

    for i in range(len(report) - 1):
        delta = report[i+1] - report[i]

        if (
            (abs(delta) < 1 or abs(delta) > 3)
            or
            (prev_delta and prev_delta * delta <= 0)
        ):
            return False

        prev_delta = delta

    return True


def is_safe_report(report):
    if evaluate_report(report):
        return True
    else:
        for i in range(len(report)):
            adjusted_report = report[:i] + report[i+1:]
            if evaluate_report(adjusted_report):
                return True

        return False


reports = [list(map(int, line.split())) for line in raw_values]
results = [is_safe_report(report) for report in reports]

safe_report_count = sum(1 for result in results if result)

print(safe_report_count)
