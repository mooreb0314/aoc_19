import sys

wires = []
for line in open('input.txt','r'):
   wires.append(line)

# test casts

#R75,D30,R83,U83,L12,D49,R71,U7,L72
#U62,R66,U55,R34,D71,R55,D58,R83

wire_1 = {
    'directions': wires[0].split(','),
    #'directions': ['R75','D30','R83','U83','L12','D49','R71','U7','L72'],
    'points': [],
    'intersections': []
}

wire_2 = {
    'directions': wires[1].split(','),
    #'directions': ['U62','R66','U55','R34','D71','R55','D58','R83'],
    'points': [],
    'intersections': []
}

def get_intersections(wire1, wire2):

    wire1_steps = 0
    wire2_steps = 0

    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    for i in range(max(len(wire1['directions']),len(wire2['directions']))):
        print("Step {}".format(i))
        wire1_direction = wire1['directions'][i]
        try:
            for _ in range(int(wire1_direction[1:])):

                wire1_steps += 1

                if wire1_direction[0] == "U":
                    y1 += 1
                elif wire1_direction[0] == "D":
                    y1 -= 1
                elif wire1_direction[0] == "L":
                    x1 -= 1
                elif wire1_direction[0] == "R":
                    x1 += 1
                else:
                    raise Exception("invalid direction")

                wire_1['points'].append({
                    'steps': wire1_steps,
                    'location': [x1,y1]
                })
        except(IndexError):
            continue
    
        try:
            wire2_direction = wire2['directions'][i]
            for _ in range(int(wire2_direction[1:])):

                wire2_steps += 1

                if wire2_direction[0] == "U":
                    y2 += 1
                elif wire2_direction[0] == "D":
                    y2 -= 1
                elif wire2_direction[0] == "L":
                    x2 -= 1
                elif wire2_direction[0] == "R":
                    x2 += 1
                else:
                    raise Exception("invalid direction")

                wire_2['points'].append({
                    'steps': wire2_steps,
                    'location': [x2,y2]
                })
        except(IndexError):
            continue


get_intersections(wire_1, wire_2)

print(len(wire_1['points']))
print(len(wire_2['points']))
distances = []
for count, point1 in enumerate(wire_1['points']):
    if len(wire_1['points']) % (count+1) == 100:
        print("Percent Done: {}%".format(count/len(wire_1['points'])*100))
    for point2 in wire_2['points']:
        if point1['location'] == point2['location']:
            wire_1['intersections'].append(point1)
            wire_2['intersections'].append(point2)
            print("Point1: {}".format(point1))
            print("Point2: {}".format(point2))
            print("Total Distance: {}".format(point1['steps'] + point2['steps']))

            distances.append(point1['steps'] + point2['steps'])

print(sorted(distances))