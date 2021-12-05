import sys


file = open("1.txt", "r")
numbers = [int(number) for number in file.read().split("\n") if len(number) != 0]
file.close()


# Part 1
last = sys.maxsize
count = 0
for number in numbers:
    if last < number:
        count += 1
    last = number
print(count)


# Part 2
last = sys.maxsize
count = 0
for i in range(0, len(numbers) - 2):
    sum = 0
    for j in range(0, 3):
        sum += numbers[i + j]
    if last < sum:
        count += 1
    last = sum
print(count)