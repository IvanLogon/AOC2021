points = []
folds = []
with open('text2.txt','r') as file:
    while True:
        line = file.readline()
        if line == '\n':
            break
        else:
            s_line = line.split(',')
            points.append([int(s_line[0]),int(s_line[1])])
    while True:
        line = file.readline()
        if line == '': 
            break
        else:
            line = line.replace('\n','')
            folds.append(line[11: len(line)])

def fold(axis, val):
    global points
    for point in points:
        if (point[axis] / val) > 1:
            point[axis] = 2*val - point[axis]

def delete_duplicates():
    global points
    temp = points
    points = []
    for point in temp:
        if point not in points:
            points.append(point)

#Part 1
for f in folds:
    f_split = f.split('=')
    fold(1 if f_split[0] == 'y' else 0, int(f_split[1]))
    delete_duplicates()
    break
print(len(points))

#Part 2
for f in folds:
    f_split = f.split('=')
    fold(1 if f_split[0] == 'y' else 0, int(f_split[1]))
    delete_duplicates()

x = []
y = []
for point in points:
    x.append(point[0])
    y.append(point[1])

matrix= []
x_max = max(x)
for i in range(max(y)+1):
    matrix.append(['.']*(x_max+1))
for i in range(len(x)):
    matrix[y[i]][x[i]] = '#'

for line in matrix:
    print(line)