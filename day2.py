import aocd


x = aocd.get_data(day=2, year=2022)


def score(a, b):
    result = ord(b) - 87
    d = ord(b) - 23 - ord(a)
    if d == 0:
        result += 3
    elif d == 1 or d == -2:
        result += 6
    return result


a = sum([score(*v.split(' ')) for v in x.split('\n')])
print(a)

aocd.submit(a, part='a', day=2, year=2022)


def score_two(a, b):
    c = a
    if b == 'X':
        c = chr(ord(a) - 1).replace('@', 'C')
    elif b == 'Z':
        c = chr(ord(a) + 1).replace('D', 'A')

    c = chr(ord(c) + 23)
    return score(a, c)


b = sum([score_two(*v.split(' ')) for v in x.split('\n')])
print(b)

aocd.submit(b, part='b', day=2, year=2022)
