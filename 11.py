class Point():
    def __init__(self, value):
        self.value = value
        self.neighbours = []
        self.light = False

    def append_neighbour(self, value):
        self.neighbours.append(value)

    def increase_light(self):
        if self.value == 9:
            self.light = True
            self.value = 0
            for point in self.neighbours:
                point.increase_light()
        elif not self.light:
            self.value += 1


def read_file():
    file = open('11.txt', 'r')
    matrix = []
    for line in file:
        matrix.append([Point(int(number))
                      for number in line.replace('\n', '')])
    file.close()
    return matrix


def bind_points(matrix, x, y):
    points = []
    for i in range(x):
        for j in range(y):
            p = matrix[i][j]
            if i + 1 < x:
                p.append_neighbour(matrix[i+1][j])
            if i - 1 >= 0:
                p.append_neighbour(matrix[i-1][j])
            if j + 1 < y:
                p.append_neighbour(matrix[i][j+1])
            if j - 1 >= 0:
                p.append_neighbour(matrix[i][j-1])
            if i + 1 < x and j + 1 < y:
                p.append_neighbour(matrix[i+1][j+1])
            if i - 1 >= 0 and j + 1 < y:
                p.append_neighbour(matrix[i-1][j+1])
            if i + 1 < x and j - 1 >= 0:
                p.append_neighbour(matrix[i+1][j-1])
            if i - 1 >= 0 and j - 1 >= 0:
                p.append_neighbour(matrix[i-1][j-1])
            points.append(p)
    return points


def main():
    # Part 1
    matrix = read_file()
    points = bind_points(matrix, len(matrix), len(matrix[0]))
    lights = []
    day = 0
    while day < 100:
        for point in points:
            point.increase_light()
        lights.append(len(list(filter(lambda o: o.value == 0, points))))
        for point in points:
            point.light = False
        day += 1
    print(sum(lights))

    # Part 2
    matrix = read_file()
    points = bind_points(matrix, len(matrix), len(matrix[0]))
    day = 0
    size = len(matrix) * len(matrix[0])
    all_zeroes = False
    while not all_zeroes:
        for point in points:
            point.increase_light()
        all_zeroes = len(list(filter(lambda o: o.value == 0, points))) == size
        for point in points:
            point.light = False
        day += 1
    print(day)

main()
