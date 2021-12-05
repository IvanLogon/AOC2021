file = open("3.txt", "r")
numbers = [int(number,2) for number in file.read().split("\n")]
file.close()

# Part 1
count = [0] * 12
for number in numbers:
    mask = 0b1
    for i in range(0, 12):
        count[i] += 1 if (number & mask) / mask == 1 else 0
        mask = mask << 1


half = len(numbers) / 2
gamma = 0
epsilon = 0
for i in range(0, 12):
    value = 1 << i
    if count[i] >= half:
        gamma += value
    else:
        epsilon += value


print(gamma * epsilon)


# Part 2
copy = numbers.copy()
mask = 2048
for i in range(11, -1, -1):
    count = 0
    for number in copy:
        count += 1 if (number & mask) > 0 else 0
    majority = 1 if count >= (len(copy)/2) else 0
    j = 0
    while j < len(copy):
        if (copy[j] & mask) / mask != majority:
            copy.pop(j)
            j -= 1
        j += 1
    if(len(copy) == 1):
        break
    mask //= 2
oxygen = copy[0]


copy = numbers.copy()
mask = 2048
for i in range(11, -1, -1):
    count = 0
    for number in copy:
        count += 1 if (number & mask) > 0 else 0
    minority = 1 if count < (len(copy)/2) else 0
    j = 0
    while j < len(copy):
        if (copy[j] & mask) / mask != minority:
            copy.pop(j)
            j -= 1
        j += 1
    if(len(copy) == 1):
        break
    mask //= 2
co2 = copy[0]


print(oxygen * co2)