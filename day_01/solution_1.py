import math

fuel = 0
for line in open('input.txt','r'):
    fuel += math.floor(int(line)/3)-2

print(fuel)