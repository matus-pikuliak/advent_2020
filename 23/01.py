cups = list(map(int, '538914762'))

v = cups[0]
cups = {
    cups[i]: cups[(i + 1) % len(cups)]
    for i
    in range(len(cups))
}

for _ in range(100):
    out = cups[v], cups[cups[v]], cups[cups[cups[v]]], v

    n = v
    while n in out:
        n = n - 1 or 9

    cups[v] = v = cups[out[2]]
    cups[out[2]] = cups[n]
    cups[n] = out[0]

res = [1]
while cups[res[-1]] != 1:
    res.append(cups[res[-1]])
print(''.join(map(str, res[1:])))