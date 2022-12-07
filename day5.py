import aocd

x = aocd.get_data(day=5, year=2022)
x = x.split('\n\n')

stacks = x[0].split('\n')[:-1]
commands = x[1].split('\n')
n_stacks = (len(stacks[0]) + 1) // 4
cols_idxs = range(1, len(stacks[0]), 4)

container = []
for i in range(n_stacks):
    stack = []
    for txt in stacks:
        v = txt[cols_idxs[i]]
        if v != ' ':
            stack.append(v)
    container.append(stack[::-1])


for cmd in commands:
    cmd = cmd.split(' ')
    n = int(cmd[1])
    from_i = int(cmd[3])
    to_i = int(cmd[5])

    from_stack = container[from_i - 1]
    to_stack =  container[to_i - 1]
    for i in range(n):
        to_stack.append(from_stack.pop())

''.join(list(map(lambda v: v[::-1][0], container)))


for cmd in commands:
    cmd = cmd.split(' ')
    n = int(cmd[1])
    from_i = int(cmd[3])
    to_i = int(cmd[5])

    from_stack = container[from_i - 1]
    to_stack = container[to_i - 1]

    tmp_stack = []
    for i in range(n):
        if len(from_stack) == 0:
            print(cmd)
            print(from_stack)
        tmp_stack.append(from_stack.pop())
    to_stack.extend(tmp_stack[::-1])










