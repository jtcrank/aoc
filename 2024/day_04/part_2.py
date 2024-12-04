###################################
# Read input values from txt file #
###################################

with open("input.txt", "r") as input_file:
    data = list(map(list, input_file.read().strip().split("\n")))

TOTAL_ROWS = len(data)
TOTAL_COLS = len(data[0])
SEARCH_PATTERNS = [
    [(-1, -1), (0, 0), (1, 1)],     # left to right diagonal
    [(-1, 1), (0, 0), (1, -1)],      # right to left diagonal
]


def extract_word_from_pattern(r, c, pattern):
    return ''.join([
        data[r + pat_r][c + pat_c]
        if (
            0 <= r + pat_r < TOTAL_ROWS
            and 0 <= c + pat_c < TOTAL_COLS
        )
        else
        ''
        for pat_r, pat_c
        in pattern
    ])


count = 0
for r, r_val in enumerate(data):
    for c, c_val in enumerate(r_val):
        if (
            c_val == 'A'
            and all([
                extract_word_from_pattern(r, c, pattern)
                in {'MAS', 'SAM'}
                for pattern
                in SEARCH_PATTERNS
            ])
        ):
            count += 1

print(count)
