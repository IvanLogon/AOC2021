class Point():
    def __init__(self, value):
        self.value = value
        self.neighbours = []
        self.visited = False

    def append_neighbour(self, value):
        self.neighbours.append(value)

    def is_low(self):
        lowest = True
        for point in self.neighbours:
            if point.value <= self.value:
                lowest = False
                break
        return lowest

    def get_basin(self):
        if self.visited:
            return 0
        else:
            self.visited = True
            sum = 0
            for neighbour in self.neighbours:
                if neighbour.value != 9:
                    sum += neighbour.get_basin()
            return sum + 1


def read_file():
    file = open('9.txt', 'r')
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
            points.append(p)
    return points


def find_low_points(points):
    low_points = []
    for point in points:
        if point.is_low():
            low_points.append(point)
    return low_points


def main():
    matrix = read_file()
    points = bind_points(matrix, len(matrix), len(matrix[0]))
    low_points = find_low_points(points)

    # Part 1
    accum = 0
    for point in low_points:
        accum += point.value
    print(accum + len(low_points))

    # Part 2
    basins = []
    for point in low_points:
        basins.append(point.get_basin())

    basins.sort(reverse=True)
    print(basins[0] * basins[1] * basins[2])


main()
