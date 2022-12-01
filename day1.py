import aocd

session = ''

x = aocd.get_data(session, day=1, year=2022)

sums = [sum([int(x) for x in elf if x != '']) for elf in map(lambda v: v.split('\n'), x.split('\n\n'))]
a = max(sums)
b = sum(sorted(sums, reverse=True)[:3])

aocd.submit(a, part='a', day=1, year=2022, session=session)
aocd.submit(b, part='b', day=1, year=2022, session=session)

