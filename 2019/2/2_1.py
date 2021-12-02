with open('input.txt') as f:
    input = f.read().splitlines()
int_code = [int(i) for i in input[0].split(',')]

for i in range(0, len(int_code), 4):
    instruction = int_code[i]
    if instruction == 99:
        break
    else:
        a = int_code[int_code[i+1]]
        b = int_code[int_code[i+2]]
        register = int_code[i+3]
        if instruction == 1:
            int_code[register] = a+b
        elif instruction == 2:
            int_code[register] = a*b
        else:
            raise Exception('Invalid Instruction')

print(int_code[0])
