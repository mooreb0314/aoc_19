wires = []
for line in open('input.txt','r'):
   wires.append(line)

wire_1 = {
    'directions': wires[0].split(','),
    'points': set()
}

wire_2 = {
    'directions': wires[1].split(','),
    'points': set()
}

def get_points(wire):
    points = []
    x = 0
    y = 0

    for direction in wire['directions']:

        for _ in range(int(direction[1:])):

            if direction[0] == "U":
                y += 1
            elif direction[0] == "D":
                y -= 1
            elif direction[0] == "L":
                x -= 1
            elif direction[0] == "R":
                x += 1
            else:
                raise Exception("invalid direction")

            points.append([x,y])
    
    return points

def get_distance(point):
    return abs(point[0]) + abs(point[1])

wire_1['points'] = {frozenset(point) for point in get_points(wire_1)}
wire_2['points'] = {frozenset(point) for point in get_points(wire_2)}

intersections = (wire_1['points'].intersection(wire_2['points']))
intersections_list = [list(intersection) for intersection in intersections]

print(min([get_distance(intersections_item) for intersections_item in intersections_list]))


