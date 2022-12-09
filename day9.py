import aocd

x = aocd.get_data(day=9, year=2022)

head_moves = x.split('\n')

# find out the maximum possible grid size to hold the state
counts = {
    'U': 0, 'R': 0, 'L': 0, 'D': 0
}

for move in head_moves:
    direction, magnitude = move.split(' ')
    counts[direction] += int(magnitude)

grid_size = max(
    counts['U'] + counts['D'],
    counts['L'] + counts['R']
)


sign = lambda x: (1, -1)[x<0]


def calc_tail_move(head_pos, tail_pos):
    hx, hy = head_pos
    tx, ty = tail_pos

    dy = hy - ty
    dx = hx - tx

    # vertical diff
    if dx == 0 and abs(dy) > 1:
        ty = ty + dy - sign(dy)

    # horizontal diff
    elif dy == 0 and abs(dx) > 1:
        tx = tx + dx - sign(dx)

    # diagonal diff
    elif (abs(dy) > 1 and abs(dx) >= 1) or (abs(dy) >= 1 and abs(dx) > 1):
        tx = tx + sign(dx)
        ty = ty + sign(dy)

    return (tx, ty)


def move_head(grid, direction, magnitude, head_pos, tails):

    for step in range(magnitude):
        if direction == 'U':
            head_pos = (head_pos[0], head_pos[1] - 1)
        elif direction == 'D':
            head_pos = (head_pos[0], head_pos[1] + 1)
        elif direction == 'L':
            head_pos = (head_pos[0]-1, head_pos[1])
        elif direction == 'R':
            head_pos = (head_pos[0]+1, head_pos[1])

        prior_head = head_pos
        for i in range(len(tails)):
            tail = tails[i]
            new_tail = calc_tail_move(prior_head, tail)
            tails[i] = new_tail
            prior_head = new_tail

        gv = grid[new_tail[1]][new_tail[0]]
        if gv == 0:
            grid[new_tail[1]][new_tail[0]] = 1

    return head_pos, tails


def swing(grid, direction, magnitude, rope):
    head = rope[0]
    tails = rope[1:]
    new_head, new_tails = move_head(grid, direction, magnitude, head, tails)
    new_rope = new_tails
    new_rope.insert(0, new_head)
    return new_rope


def do_count(n):
    grid = [[0 for j in range(grid_size)] for i in range(grid_size)]
    start_pos = grid_size//2

    rope = [(start_pos, start_pos) for i in range(n)]
    grid[start_pos][start_pos] = 1

    for move in head_moves:
        direction, magnitude = move.split(' ')
        magnitude = int(magnitude)
        rope = swing(grid, direction, magnitude, rope)

    return sum(map(sum, grid))


a = do_count(2)
b = do_count(10)



