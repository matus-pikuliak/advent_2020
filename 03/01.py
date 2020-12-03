row_len = len(next(open('input'))) - 1

print(
    sum(
        line[i * 3 % row_len] == '#'
        for i, line
        in enumerate(open('input'))
    )
)
