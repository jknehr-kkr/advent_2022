import aocd

x = aocd.get_data(day=10, year=2022)

cmds = x.split('\n')


checkpoints = [20, 60, 100, 140, 180, 220]
register = 2
cycle = 1
a = 0

crt = [0]*240


for cmd in cmds:

    if cmd == 'noop':
        cmd_cyles = 1
    else:
        cmd_cyles = 2

    for i in range(cmd_cyles):

        if abs(register - cycle % 40) <= 1:
            print(register, cycle)
            crt[cycle - 1] = 1

        if cycle in checkpoints:
            a += cycle * register

        cycle += 1

    if cmd.startswith('addx'):
        v = int(cmd.split(' ')[1])
        register += v


for i in range(len(crt)):
    d = '#' if crt[i] > 0 else ' '
    end = ''
    if i != 0 and (i+1) % 40 == 0:
        end = '\n'
    print(d, end=end, flush=True)



