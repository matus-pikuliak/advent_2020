def pass_id(seat):
    row = sum(
        2 ** (6-i)
        for i, c
        in enumerate(seat[:7])
        if c == 'B'
    )
    col = sum(
        2 ** (2 - i)
        for i, c
        in enumerate(seat[7:])
        if c == 'R'
    )
    return 8 * row + col


ids = set(map(pass_id, open('input')))

for id in ids:
    if id + 1 not in ids and id + 2 in ids:
        print(id + 1)
