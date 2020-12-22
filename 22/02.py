lines = open('input').readlines()
p1 = list(map(int, lines[1:26]))
p2 = list(map(int, lines[28:]))


def game(p1, p2):
    history = set()

    while p1 and p2:

        hsh = tuple(p1 + [0] + p2)
        if hsh in history:
            return p1, p2, 1
        history.add(hsh)

        c1, c2 = p1.pop(0), p2.pop(0)
        if len(p1) < c1 or len(p2) < c2:
            w = c1 > c2
        else:
            _, _, w = game(p1[:c1], p2[:c2])

        if w:
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])

    return p1, p2, bool(p1)


p1, p2, _ = game(p1, p2)

print(
    sum(
        c * w
        for c, w
        in zip(p1 or p2, range(50, 0, -1))
    )
)
