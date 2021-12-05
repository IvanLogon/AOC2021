file = open("5.txt", "r")
lines = [line for line in file.read().split("\n")]
file.close()

def map_terrain(vectors):
    terrain = {}
    for vector in vectors:
        x1, y1 = vector[0]
        x2, y2 = vector[1]
        xstep = 1 if x1 <= x2 else -1
        ystep = 1 if y1 <= y2 else -1
        exit = False
        while not exit:
            if terrain.get((x1,y1)) is None:
                terrain[(x1,y1)] = 1
            else:
                terrain[(x1,y1)] += 1
            
            exit = ((x1 == x2) and (y1 == y2))

            if x1 != x2: x1 += xstep
            if y1 != y2: y1 += ystep
    return terrain

def count_intersections(terrain):
    count = 0
    for space in terrain:
        if terrain[space] > 1:
            count += 1
    return count

def main():
    #Part 1
    vectors = []
    for line in lines:
        values = line.split(' -> ')
        v1 = [int(number) for number in values[0].split(',')]
        v2 = [int(number) for number in values[1].split(',')]
        if v1[0] == v2[0] or v1[1] == v2[1]:
            vectors.append([v1, v2])

    terrain = map_terrain(vectors)
    print(count_intersections(terrain))


    #Part 2
    vectors = []
    for line in lines:
        values = line.split(' -> ')
        v1 = [int(number) for number in values[0].split(',')]
        v2 = [int(number) for number in values[1].split(',')]
        if v1[0] == v2[0] or v1[1] == v2[1]:
            vectors.append([v1, v2])
        elif abs((v2[0] - v1[0]) // (v2[1] - v1[1])) == 1:
            vectors.append([v1, v2])

    terrain = map_terrain(vectors)
    print(count_intersections(terrain))

main()