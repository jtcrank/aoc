from itertools import groupby

####################
# Bingo Card Class #
####################
class BingoCard(object):
    def __init__(self, card_data):
        self.grid = [ [int(col) for col in row.split()] for row in card_data ]
        self.is_winner = False
        self.score = 0

    def stamp(self, number):
        for row_idx, row in enumerate(self.grid):
            for col_idx, col_val in enumerate(row):
                if col_val == number:
                    self.grid[row_idx][col_idx] = f'({col_val})'
                    return self._check_win(number, row_idx, col_idx)


    def _check_win(self, number, row_idx, col_idx):
        if (
            all([ type(i) == str for i in self.grid[row_idx] ])
            or all([ type(i) == str for i in list(map(list, zip(*self.grid)))[col_idx] ])
        ):
            self.is_winner = True
            self._calculate_score(number)

        return self.is_winner


    def print_card(self):
        for row_idx, row in enumerate(self.grid):
            for col_idx, col_val in enumerate(row):
                print('{:6}'.format(str(col_val)), end='')
            print()


    def _calculate_score(self, winning_number):
        base_score = sum([ col_val for row in self.grid for col_val in row if type(col_val) == int])
        self.score = base_score * winning_number


#########
# Setup #
#########
with open('input.txt') as f:
    bingo_setup = [ line for line in f.read().splitlines() ]

numbers = [ int(i) for i in bingo_setup.pop(0).split(',') ]

cards = [ BingoCard(list(sub)) for ele, sub in groupby(bingo_setup, key = bool) if ele ]

#############
# Play Game #
#############
for num in numbers:
    for card in cards:
        if card.stamp(num):
            print('Winning Card:')
            card.print_card()
            print(f'\nScore: {card.score}')
            exit()
