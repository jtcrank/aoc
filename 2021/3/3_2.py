with open('input.txt') as f:
    diagnostics = [ [int(i) for i in list(line)] for line in f.read().splitlines() ]


def filter_codes(diagnostics, criteria, pos=0):
    bit_column = [ i[pos] for i in diagnostics ]
    if criteria == 'max':
        key_bit = 1 if bit_column.count(1) >= bit_column.count(0) else 0
    elif criteria == 'min':
        key_bit = 0 if bit_column.count(0) <= bit_column.count(1) else 1

    filtered_diagnostics = list(filter(lambda x: x[pos] == key_bit, diagnostics))
    if len(filtered_diagnostics) == 1:
        return int(''.join([str(i) for i in filtered_diagnostics[0]]), 2)
    else:
        return filter_codes(filtered_diagnostics, criteria, pos+1)

oxygen = filter_codes(diagnostics, 'max')
co2 = filter_codes(diagnostics, 'min')
print(f'Life Support Rating: {oxygen * co2} (oxygen-{oxygen} | CO2-{co2})')

