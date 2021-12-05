def read_file():
    file = open("3.txt", "r")
    numbers = [int(number,2) for number in file.read().split("\n")]
    file.close()
    return numbers


def count(copy, mask):
    count = 0
    for number in copy:
        if number & mask > 0:
            count += 1
    return count

def filter_binary(copy, mask, value):
    j = 0
    while j < len(copy):
        if (copy[j] & mask) / mask != value:
            copy.pop(j)
            j -= 1
        j += 1


def get_oxygen(numbers):
    copy = numbers.copy()
    mask = 2048
    while not len(copy) == 1:
        majority = 1 if count(copy, mask) >= (len(copy)/2) else 0
        filter_binary(copy, mask, majority)
        mask //= 2
    return copy[0]


def get_co2(numbers):
    copy = numbers.copy()
    mask = 2048
    while not (len(copy) == 1):
        minority = 1 if count(copy, mask) < (len(copy)/2) else 0
        filter_binary(copy, mask, minority)
        mask //= 2
    return copy[0]


def main():
    numbers = read_file()


    # Part 1
    count = [0] * 12
    for number in numbers:
        mask = 0b1
        for i in range(0, 12):
            count[i] += 1 if (number & mask) > 0 else 0
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
    print(gamma*epsilon)


    # Part 2
    print(get_oxygen(numbers) * get_co2(numbers))

main()