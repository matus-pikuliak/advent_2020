cups = list(map(int, '538914762'))
cups += [i for i in range(10, 10**6+1)]

v = cups[0]
cups = {
    cups[i]: cups[(i + 1) % len(cups)]
    for i
    in range(len(cups))
}

for _ in range(10**7):
    out = cups[v], cups[cups[v]], cups[cups[cups[v]]], v

    n = v
    while n in out:
        n = n - 1 or 10 ** 6

    cups[v] = v = cups[out[2]]
    cups[out[2]] = cups[n]
    cups[n] = out[0]

print(cups[1]*cups[cups[1]])
