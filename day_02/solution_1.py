for line in open('input.txt','r'):
    intcodes = line.split(',')

program = [int(intcode) for intcode in intcodes]

for index, opcode in enumerate(program):
    if index % 4 != 0:
        continue

    if opcode == 99:
        break

    noun, verb, answer = program[index + 1 : index + 4]
    if opcode == 1:
        # add
        program[answer] = program[noun] + program[verb]
    elif opcode == 2:
        # multiply
        program[answer] = program[noun] * program[verb]
    else:
        print("ERROR")

print(program)