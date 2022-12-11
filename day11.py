# import aocd

# x = aocd.get_data(day=11, year=2022)

# raw_monkeys = x.split('\n\n')


def get_monkeys():
    return [
        {
            'items': [98, 89, 52][::-1],
            'operation': lambda v: v * 2,
            'test': lambda v: 6 if v % 5 == 0 else 1,
            'inspection_count': 0
        },
        {
            'items': [57, 95, 80, 92, 57, 78],
            'operation': lambda v: v * 13,
            'test': lambda v: 2 if v % 2 == 0 else 6,
            'inspection_count': 0
        },
        {
            'items': [82, 74, 97, 75, 51, 92, 83],
            'operation': lambda v: v + 5,
            'test': lambda v: 7 if v % 19 == 0 else 5,
            'inspection_count': 0
        },
        {
            'items': [97, 88, 51, 68, 76],
            'operation': lambda v: v + 6,
            'test': lambda v: 0 if v % 7 == 0 else 4,
            'inspection_count': 0
        },
        {
            'items': [63],
            'operation': lambda v: v + 1,
            'test': lambda v: 0 if v % 17 == 0 else 1,
            'inspection_count': 0
        },
        {
            'items': [94, 91, 51, 63],
            'operation': lambda v: v + 4,
            'test': lambda v: 4 if v % 13 == 0 else 3,
            'inspection_count': 0
        },
        {
            'items': [61, 54, 94, 71, 74, 68, 98, 83],
            'operation': lambda v: v + 2,
            'test': lambda v: 2 if v % 3 == 0 else 7,
            'inspection_count': 0
        },
        {
            'items': [90, 56],
            'operation': lambda v: v * v,
            'test': lambda v: 3 if v % 11 == 0 else 5,
            'inspection_count': 0
        }
    ]


monkeys = get_monkeys()
rounds = 10000

for round in range(rounds):
    if round % 50 == 0:
        print(round)
        print(sorted(list(map(lambda v: v['inspection_count'], monkeys)), reverse=True))
    for monkey in monkeys:
        for i in range(len(monkey['items'])):
            item = monkey['items'].pop(0)
            item = monkey['operation'](item)
            # item = item // 3
            item = item % 9699690
            monkey['inspection_count'] += 1
            monkeys[monkey['test'](item)]['items'].append(item)
print('finished')


print(sorted(list(map(lambda v: v['inspection_count'], monkeys)), reverse=True)[0:2])




