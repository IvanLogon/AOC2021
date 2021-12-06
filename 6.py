def read_file():
    file = open('6.txt', 'r')
    numbers = [int(number) for number in file.read().split(',')]
    file.close()
    return numbers


def initialize():
    days = read_file()
    timer = [0]*10
    for day in days:
        timer[day] += 1
    return timer


def populate(timer, days):
    day = 0
    while day < days:
        for i in range(0,10):
            value = timer[i]
            if i == 0:
                timer[7] += value
                timer[9] += value
            else:
                timer[i-1] += value
            timer[i] -= value
        day += 1


def main():
    #Part 1
    timer = initialize()
    # Cycle
    populate(timer, 80)
    # Count
    print(sum(timer))

    #Part 2
    timer = initialize()
    # Cycle
    populate(timer, 256)
    # Count
    print(sum(timer))

main()