import math

def get_fuel(mass, curr_fuel=0):
    
    f = math.floor(int(mass)/3)-2
    print(f)
    if f < 0:
        f = 0

    curr_fuel += f
    if f == 0:
        #print(curr_fuel)
        return curr_fuel
    else:
        #print(curr_fuel)
        return get_fuel(f, curr_fuel)

fuel = 0
for line in open('input.txt','r'):
    fuel += get_fuel(int(line))

print(get_fuel(1969))

print(fuel)