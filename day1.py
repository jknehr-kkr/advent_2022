import aocd

x = aocd.get_data(day=1, year=2022)

sums = [sum([int(x) for x in elf if x != '']) for elf in map(lambda v: v.split('\n'), x.split('\n\n'))]
a = max(sums)
b = sum(sorted(sums, reverse=True)[:3])
print(a, b)

aocd.submit(a, part='a', day=1, year=2022)
aocd.submit(b, part='b', day=1, year=2022)

