def read_file():
    file = open('7.txt', 'r')
    numbers = [int(number) for number in file.read().split(',')]
    file.close()
    return numbers


def fuel_calculation(position):
    return position * (position + 1) >> 1


def main():
    numbers = read_file()
    biggest = max(numbers)


    #Part 1
    totals = []
    for i in range(0, biggest + 1):
        totals.append(sum(map(lambda n: abs(n - i), numbers)))
    print(min(totals))


    #Part 2
    totals = []
    for i in range(0, biggest + 1):
        totals.append(sum(map(lambda n: fuel_calculation(abs(n - i)), numbers)))
    print(min(totals))


main()