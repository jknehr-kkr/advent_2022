
import aocd
x = aocd.get_data(day=8, year=2022)
x = x.split('\n')

grid = [list(map(lambda v: int(v), list(s))) for s in x]
grid_t = list(zip(*grid)) # transpose the grid for easier row-wise searching
nc = len(grid[0])
nr = len(grid)


def is_visible(i, j):
    value = grid[i][j]

    # search right
    if value > max(grid[i][j+1:]):
        return 1

    # search left
    if value > max(grid[i][0:j]):
        return 1

    # search top
    if value > max(grid_t[j][0:i]):
        return 1

    if value > max(grid_t[j][i+1:]):
        return 1

    return 0


cum = 0
for i in range(1, nr-1):
    for j in range(1, nc-1):
        cum += is_visible(i, j)

a = nc*2 + nr*2 - 4 + cum


def tree_count(v, trees):
    c = 0
    for tree in trees:
        c += 1
        if tree >= v:
            return c
    return c


def scenic_score(i, j):
    value = grid[i][j]
    score = 1
    score *= tree_count(value, grid[i][j+1:])
    score *= tree_count(value, grid[i][0:j][::-1])
    score *= tree_count(value, grid_t[j][0:i][::-1])
    score *= tree_count(value, grid_t[j][i+1:])
    return score


max_score = 0
for i in range(1, nr-1):
    for j in range(1, nc-1):
        score = scenic_score(i, j)
        max_score = max(score, max_score)

b = max_score


