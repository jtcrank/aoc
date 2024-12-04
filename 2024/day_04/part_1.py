###################################
# Read input values from txt file #
###################################

with open("input.txt", "r") as input_file:
    data = list(map(list, input_file.read().strip().split("\n")))

TOTAL_ROWS = len(data)
TOTAL_COLS = len(data[0])
SEARCH_PATTERNS = [
    [(-1, 0), (-2, 0), (-3, 0)],        # up
    [(1, 0), (2, 0), (3, 0)],           # down
    [(0, -1), (0, -2), (0, -3)],        # left
    [(0, 1), (0, 2), (0, 3)],           # right
    [(-1, -1), (-2, -2), (-3, -3)],     # up left
    [(-1, 1), (-2, 2), (-3, 3)],        # up right
    [(1, -1), (2, -2), (3, -3)],        # down left
    [(1, 1), (2, 2), (3, 3)],           # down right
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
        in [(0, 0), *pattern]
    ])


count = 0
for r, r_val in enumerate(data):
    for c, c_val in enumerate(r_val):
        if c_val == 'X':
            count += sum([
                extract_word_from_pattern(r, c, pattern) == 'XMAS'
                for pattern
                in SEARCH_PATTERNS
            ])

print(count)
