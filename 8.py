def read_file():
    file = open('8.txt', 'r')
    pairs = [[pair for pair in line.split(' | ')]
             for line in file.read().split('\n')]
    file.close()
    inputs = []
    outputs = []
    for pair in pairs:
        inputs.append(pair[0].split(' '))
        outputs.append(pair[1].split(' '))
    return inputs, outputs


def decode(input):
    '''
     000
    6   1
    6   1
     555
    4   2
    4   2
     333
    '''
    display = ['']*7
    input.sort(key=lambda i: len(i))
    # Decode 7 and 1
    for i in range(3):
        if input[1][i] in input[0]:
            display[1] += input[1][i]
            display[2] += input[1][i]
        else:
            display[0] = input[1][i]
    # Decode 4
    for i in range(4):
        if input[2][i] not in display[1]:
            display[5] += input[2][i]
            display[6] += input[2][i]
    # Decode 8
    for i in range(7):
        letter = input[9][i]
        if letter not in display[1] and letter not in display[5] and letter not in display[0]:
            display[3] += input[9][i]
            display[4] += input[9][i]
    # Get 5 signal and determine displays 1,2,3,4
    for signal in input[3:6]:
        if display[5][0] in signal and display[5][1] in signal:
            # displays 1 and 2
            seg_2 = ''
            for letter in display[1]:
                if letter in signal:
                    seg_2 = letter
                    break
            display[1] = display[1].replace(seg_2, '')
            display[2] = seg_2
            # displays 3 and 4
            seg_3 = ''
            for letter in display[3]:
                if letter in signal:
                    seg_3 = letter
                    break
            display[3] = seg_3
            display[4] = display[4].replace(seg_3, '')
    # Get 2 signal and determine displays 5,6
    for signal in input[3:6]:
        if display[4] in signal:
            # displays 5 and 6
            seg_5 = ''
            for letter in display[5]:
                if letter in signal:
                    seg_5 = letter
                    break
            display[5] = seg_5
            display[6] = display[6].replace(seg_5, '')
    return display


def get_positions_on_display(display, outputs):
    positions = []
    for output in outputs:
        position = []
        for letter in output:
            position.append(display.index(letter))
            position.sort()
        positions.append(position)
    return positions


def get_number(positions):
    values = [
        [0, 1, 2, 3, 4, 6],
        [1, 2],
        [0, 1, 3, 4, 5],
        [0, 1, 2, 3, 5],
        [1, 2, 5, 6],
        [0, 2, 3, 5, 6],
        [0, 2, 3, 4, 5, 6],
        [0, 1, 2],
        [0, 1, 2, 3, 4, 5, 6],
        [0, 1, 2, 3, 5, 6]
    ]
    number = 0
    unit = 1000
    for position in positions:
        for i in range(10):
            if values[i] == position:
                number += (i*unit)
                unit //= 10
    return number


def main():
    inputs, outputs = read_file()

    # Part 1
    accum = 0
    for output in outputs:
        accum += len(list(filter(lambda d: [2, 3, 4,
                     7].count(d), map(lambda d: len(d), output))))
    print(accum)

    # Part 2
    numbers = []
    for i in range(len(inputs)):
        display = decode(inputs[i])
        positions = get_positions_on_display(display, outputs[i])
        number = get_number(positions)
        numbers.append(number)
    print(sum(numbers))


main()
