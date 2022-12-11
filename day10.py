import aocd

x = aocd.get_data(day=10, year=2022)

cmds = x.split('\n')


checkpoints = [20, 60, 100, 140, 180, 220]
register = 2
cycle = 1
a = 0

crt = [0]*240


test_cmds = [
'addx 15',
'addx -11',
'addx 6',
'addx -3',
'addx 5',
'addx -1',
'addx -8',
'addx 13',
'addx 4',
'noop',
'addx -1',
'addx 5',
'addx -1',
'addx 5',
'addx -1',
'addx 5',
'addx -1',
'addx 5',
'addx -1',
'addx -35',
'addx 1',
'addx 24',
'addx -19',
'addx 1',
'addx 16',
'addx -11',
'noop',
'noop',
'addx 21',
'addx -15',
'noop',
'noop',
'addx -3',
'addx 9',
'addx 1',
'addx -3',
'addx 8',
'addx 1',
'addx 5',
'noop',
'noop',
'noop',
'noop',
'noop',
'addx -36',
'noop',
'addx 1',
'addx 7',
'noop',
'noop',
'noop',
'addx 2',
'addx 6',
'noop',
'noop',
'noop',
'noop',
'noop',
'addx 1',
'noop',
'noop',
'addx 7',
'addx 1',
'noop',
'addx -13',
'addx 13',
'addx 7',
'noop',
'addx 1',
'addx -33',
'noop',
'noop',
'noop',
'addx 2',
'noop',
'noop',
'noop',
'addx 8',
'noop',
'addx -1',
'addx 2',
'addx 1',
'noop',
'addx 17',
'addx -9',
'addx 1',
'addx 1',
'addx -3',
'addx 11',
'noop',
'noop',
'addx 1',
'noop',
'addx 1',
'noop',
'noop',
'addx -13',
'addx -19',
'addx 1',
'addx 3',
'addx 26',
'addx -30',
'addx 12',
'addx -1',
'addx 3',
'addx 1',
'noop',
'noop',
'noop',
'addx -9',
'addx 18',
'addx 1',
'addx 2',
'noop',
'noop',
'addx 9',
'noop',
'noop',
'noop',
'addx -1',
'addx 2',
'addx -37',
'addx 1',
'addx 3',
'noop',
'addx 15',
'addx -21',
'addx 22',
'addx -6',
'addx 1',
'noop',
'addx 2',
'addx 1',
'noop',
'addx -10',
'noop',
'noop',
'addx 20',
'addx 1',
'addx 2',
'addx 2',
'addx -6',
'addx -11',
'noop',
'noop',
'noop',
]


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



