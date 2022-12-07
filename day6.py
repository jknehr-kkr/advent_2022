import aocd

x = aocd.get_data(day=6, year=2022)


for i in range(14, len(x)):
    if len(set(x[i-14:i])) == 14:
        print(i)
        break


