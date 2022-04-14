from collections import Counter


def read_file():
    polymeter = None
    pairs = {}
    with open('14.txt', 'r') as file:
        polymeter = list(file.readline())[:-1]
        file.readline()
        while True:
            line = file.readline()
            if line == '':
                break
            else:
                line = line.replace('\n', '').split(' -> ')
                pairs[line[0]] = line[1]
    return polymeter, pairs


def part1(polymeter, pairs):
    for _ in range(10):
        length = 2*len(polymeter) - 2
        for i in range(0, length, 2):
            combination = polymeter[i] + polymeter[i + 1]
            polymeter.insert(i + 1, pairs[combination])

    counter = Counter(polymeter)
    values = counter.values()
    return max(values) - min(values)


def main():
    polymeter, pairs = read_file()
    result = part1(polymeter, pairs)
    print(result)

main()