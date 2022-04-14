def read_file():
    points = []
    folds = []
    with open('13.txt', 'r') as file:
        while True:
            line = file.readline()
            if line == '\n':
                break
            else:
                s_line = line.split(',')
                points.append([int(s_line[0]), int(s_line[1])])
        while True:
            line = file.readline()
            if line == '':
                break
            else:
                line = line.replace('\n', '')
                folds.append(line[11: len(line)])
    return points, folds


def fold(points, axis, val):
    for point in points:
        if (point[axis] / val) > 1:
            point[axis] = 2*val - point[axis]


def delete_duplicates(array):
    points = []
    for point in array:
        if point not in points:
            points.append(point)
    return points

# Part 1


def part1(points, folds):
    for f in folds:
        f_split = f.split('=')
        fold(points, 1 if f_split[0] == 'y' else 0, int(f_split[1]))
        points = delete_duplicates(points)
        break
    return len(points)

# Part 2


def part2(points, folds):
    for f in folds:
        f_split = f.split('=')
        fold(points, 1 if f_split[0] == 'y' else 0, int(f_split[1]))
        points = delete_duplicates(points)

    x = []
    y = []
    for point in points:
        x.append(point[0])
        y.append(point[1])

    matrix = []
    x_max = max(x)
    for i in range(max(y)+1):
        matrix.append(['.']*(x_max+1))
    for i in range(len(x)):
        matrix[y[i]][x[i]] = '#'

    for line in matrix:
        print(line)


def main():
    points, folds = read_file()
    result = part1(points, folds)
    print(result)

    points, folds = read_file()
    part2(points, folds)


main()
