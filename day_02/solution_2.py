for line in open('input.txt','r'):
    intcodes = line.split(',')

program = [int(intcode) for intcode in intcodes]

for i in range(100):
    for j in range(100):
        copy = program[:]
        copy[1], copy[2] = i,j
        for address, opcode in enumerate(copy):
            if address % 4 != 0:
                continue
            if opcode == 99:
                break

            noun, verb, answer = copy[address + 1 : address + 4]
            if opcode == 1:
                # add
                copy[answer] = copy[noun] + copy[verb]
            elif opcode == 2:
                # multiply
                copy[answer] = copy[noun] * copy[verb]
            else:
                print("ERROR")

            if copy[0] == 19690720:
                print("Noun: {0}, Verb: {1}".format(i,j))
                print(100 * i + j)


