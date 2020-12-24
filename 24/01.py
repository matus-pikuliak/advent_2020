import re

tiles = dict()

for line in open('input').read().splitlines():
    t = 0j
    for dir in re.findall(r'([ns]?[we])', line):
        t += {
            'e': 1j,
            'w': -1j,
            'ne': 1j - 1,
            'nw': -1,
            'se': 1,
            'sw': -1j + 1
        }[dir]
    tiles[t] = not tiles.get(t, False)

print(sum(tiles.values()))
