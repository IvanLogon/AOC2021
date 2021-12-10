def read_file():
    file = open('10.txt', 'r')
    lines = [line for line in file.read().split('\n')]
    file.close()
    return lines


def check_sintax(line):
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    stack = []
    for character in line:
        if character in ['(', '[', '{', '<']:
            stack.append(character)
        else:
            if pairs[stack.pop()] != character:
                return False, character
    return True, None


def fix_line(line):
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    stack = []
    fix_stack = []
    for character in line:
        if character in ['(', '[', '{', '<']:
            stack.append(character)
        else:
            stack.pop()

    for character in stack:
        fix_stack.insert(0, pairs[character])
    return fix_stack


def error_score(errors):
    pairs = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    accum = 0
    for error in errors:
        accum += pairs[error]
    return accum


def fix_score(fix):
    pairs = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    accum = 0
    for character in fix:
        accum = accum * 5 + pairs[character]
    return accum


def main():
    # Part 1
    lines = read_file()
    incorrect_lines = []
    errors = []
    while len(lines) > 0:
        line = lines.pop()
        correct, character = check_sintax(line)
        if not correct:
            errors.append(character)
        else:
            incorrect_lines.append(line)
    score = error_score(errors)
    print(score)

    # Part 2
    fixes = []
    for line in incorrect_lines:
        fixes.append(fix_line(line))
    fix_scores = []
    for fix in fixes:
        fix_scores.append(fix_score(fix))
    fix_scores.sort()
    print(fix_scores[len(fix_scores)//2])


main()
