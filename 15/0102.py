mem = {
    int(v): i
    for i, v
    in enumerate(open('input').read().split(', '))
}
dif = 0

for i in range(7, 30_000_000):
    val = dif
    dif = dif in mem and i - mem[dif]
    mem[val] = i
    if i == 2019:
        print('Part 1:', val)

print('Part 2:', val)
