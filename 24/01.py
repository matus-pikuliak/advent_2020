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

print(len(black))
