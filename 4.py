def read_file():
    file = open("4.txt", "r")
    bingo = file.read().split("\n\n")
    file.close()
    return bingo


def get_cardboards(bingo):
    cardboards = []
    for matrix in bingo[1:]:
        lines = matrix.split("\n")
        cardboard = []
        for line in lines:
            cardboard.append([[int(number), 0] for number in line.split()])
        cardboards.append(cardboard)
    return cardboards


def check_row(row):
    for number in row:
        if number[1] == 0:
            return False
    return True


def check_column(cardboard):
    for i in range(0, 5):
        count = 0
        for row in cardboard:
            if row[i][1] == 1:
                count += 1
        if count == 5:
            return True
    return False


def main():
    bingo = read_file()
    serie = [int(number) for number in bingo[0].split(',')]

    # Part 1
    cardboards = get_cardboards(bingo)
    winnerCardboard = None
    number = 0
    for number in serie:
        for cardboard in cardboards:
            for row in cardboard:
                for cell in row:
                    if cell[0] == number:
                        cell[1] = 1
                        winner = check_row(row) or check_column(cardboard)
                        if winner:
                            winnerCardboard = cardboard
                        break
                if winnerCardboard:
                    break
            if winnerCardboard:
                break
        if winnerCardboard:
            break
    sum = 0
    for row in winnerCardboard:
        for cell in row:
            if cell[1] == 0:
                sum += cell[0]
    print(sum * number)

    # Part 2
    cardboards = []
    for cardboard in get_cardboards(bingo):
        cardboards.append([0, cardboard])
    number = 0
    lastwinner = None
    for number in serie:
        for cardboard in cardboards:
            winner = False
            if cardboard[0] == 0:
                for row in cardboard[1]:
                    for cell in row:
                        if cell[0] == number:
                            cell[1] = 1
                            winner = check_row(
                                row) or check_column(cardboard[1])
                            if len(list(filter(lambda c: c[0] == 0, cardboards))) == 1 and winner:
                                lastwinner = cardboard[1]
                            break
                        if winner:
                            break
                if winner:
                    cardboard[0] = 1
        if len(list(filter(lambda c: c[0] == 0, cardboards))) == 0: break
    sum = 0
    for row in lastwinner:
        print(row)
        for cell in row:
            if cell[1] == 0:
                sum += cell[0]
    print(sum * number)


main()
