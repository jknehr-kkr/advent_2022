import aocd

sacks = aocd.get_data(day=3, year=2022).split('\n')

score = lambda v: ord(v)-96 if ord(v) > 96 else ord(v)-38

shared = [list(set(sack[0:len(sack)//2]) & set(sack[len(sack)//2:len(sack)])) for sack in sacks]

a = sum(map(score, map(lambda v: ''.join(v), shared)))
aocd.submit(a, part='a', day=3, year=2022)

b = sum(map(score, [(set(sacks[i]) & set(sacks[i+1]) & set(sacks[i+2])).pop() for i in list(range(0, len(sacks), 3))]))
aocd.submit(b, part='b', day=3, year=2022)
