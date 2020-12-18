from operator import add, mul


def val(t):
    if (c := next(t)) == '(':
        return parse(t)
    return int(c)


def parse(t):
    v = val(t)
    while (c := next(t)) not in [')', '\n']:
        v = {'+': add, '*': mul}[c](v, val(t))
    return v

print(
    sum(
        parse(iter(line.replace(' ', '')))
        for line
        in open('input')
    )
)
