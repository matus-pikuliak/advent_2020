cups = list(map(int, '538914762'))
v = cups[0]

for s in range(100):
    out = [cups.pop((cups.index(v)+1) % len(cups)) for _ in range(3)]

    n = v - 1
    while n % 10 not in cups:
        n -= 1

    for i in range(3):
        cups.insert(cups.index(n % 10) + i + 1, out[i])

    v = cups[(cups.index(v) + 1) % 9]

print(''.join(map(str, cups))*2)
