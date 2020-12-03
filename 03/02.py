from math import prod

row_len = len(next(open('input'))) - 1

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

trees = [
    sum(
        line[i // down * right % row_len] == '#'
        for i, line
        in enumerate(open('input'))
        if i % down == 0
    )
    for right, down
    in slopes
]

print(prod(trees))
