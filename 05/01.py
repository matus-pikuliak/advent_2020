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


print(
    max(
        map(pass_id, open('input'))
    )
)
