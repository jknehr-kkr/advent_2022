import aocd

x = aocd.get_data(day=4, year=2022).split('\n')


def score(a, b):
    a_lb, a_ub = a.split('-')
    b_lb, b_ub = b.split('-')
    a_lb, a_ub, b_lb, b_ub = int(a_lb), int(a_ub), int(b_lb), int(b_ub)

    if a_lb <= b_lb and a_ub >= b_ub:
        return 1

    if b_lb <= a_lb and b_ub >= a_ub:
        return 1

    return 0


a = sum([score(*v.split(',')) for v in x])


def score2(a, b):
    a_lb, a_ub = a.split('-')
    b_lb, b_ub = b.split('-')
    a_lb, a_ub, b_lb, b_ub = int(a_lb), int(a_ub), int(b_lb), int(b_ub)

    if a_lb <= b_lb <= a_ub:
        return 1

    if a_lb <= b_ub <= a_ub:
        return 1

    if b_lb <= a_lb <= b_ub:
        return 1

    if b_lb <= a_ub <= b_ub:
        return 1
    return 0


b = sum([score2(*v.split(',')) for v in x])
