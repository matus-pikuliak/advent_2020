lines = open('input').readlines()
p1 = list(map(int, lines[1:26]))
p2 = list(map(int, lines[28:]))

while p1 and p2:
    c1, c2 = p1.pop(0), p2.pop(0)
    if c1 > c2:
        p1.extend([c1, c2])
    else:
        p2.extend([c2, c1])

print(
    sum(
        c * w
        for c, w
        in zip(p1 or p2, range(50, 0, -1))
    )
)
