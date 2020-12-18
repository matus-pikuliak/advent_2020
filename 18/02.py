from math import prod


def val(t):
    if (c := next(t)) == '(':
        return parse(t)
    return int(c)


def parse(t):
    vals = [val(t)]
    while (c := next(t)) not in [')', '\n']:
        if c == '*':
            vals.append(val(t))
        else:
            vals[-1] += val(t)
    return prod(vals)


print(
    sum(
        parse(iter(line.replace(' ', '')))
        for line
        in open('input')
    )
)
