import re

dirs = {
    'e': 1j,
    'w': -1j,
    'ne': 1j - 1,
    'nw': -1,
    'se': 1,
    'sw': -1j + 1
}

black = set()
for line in open('input').read().splitlines():
    black ^= {
        sum(
            dirs[dir]
            for dir
            in re.findall(r'([ns]?[we])', line)
        )
    }


def neighbours(point):
    return set(
        point + dif
        for dif
        in dirs.values()
    )


for _ in range(100):
    black = set(
        p
        for p
        in set.union(*[neighbours(b) for b in black])
        if (an := len(black & neighbours(p))) == 2 or p in black and an == 1
    )

print(len(black))
