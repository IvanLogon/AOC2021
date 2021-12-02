file = open("2.txt", "r")
routines_raw = file.read().split("\n")
file.close()
routines = []
for routine in routines_raw:
    parts = routine.split(' ')
    routines.append([parts[0], int(parts[1])])


# Part 1
x = 0
y = 0
for routine in routines:
    direction = routine[0]
    if direction == 'forward':
        x += routine[1]
    elif direction == 'down':
        y += routine[1]
    else:
        y -= routine[1]


print(x * y)


# Part 2
x = 0
y = 0
aim = 0
for routine in routines:
    direction = routine[0]
    if direction == 'forward':
        x += routine[1]
        y += aim * routine[1]
    elif direction == 'down':
        aim += routine[1]
    else:
        aim -= routine[1]


print(x * y)