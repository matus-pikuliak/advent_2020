from itertools import product


def neighbours(point):
    return set(
        tuple(p + d for p, d in zip(point, dif))
        for dif
        in product([-1, 0, 1], repeat=4)
        if any(dif)
    )


active = set(
    (i, j, 0, 0)
    for i, line in enumerate(open('input'))
    for j, c in enumerate(line.strip())
    if c == '#'
)

for _ in range(6):
    active = set(
        p
        for p
        in set.union(*[neighbours(a) for a in active])
        if (an := len(active & neighbours(p))) == 3 or p in active and an == 2
    )

print(len(active))
