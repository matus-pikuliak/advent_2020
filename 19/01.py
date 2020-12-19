from functools import cache
from itertools import product

rules = dict(
    line.split(': ')
    for line
    in open('rules').read().splitlines()
)

@cache
def valid(rule):
    if '"' in rule:
        return set(rule[1])
    if '|' in rule:
        return set.union(*map(valid, rule.split(' | ')))
    if ' ' in rule:
        l, r = rule.split()
        return set(
            a + b
            for a, b
            in product(valid(l), valid(r))
        )
    return valid(rules[rule])


print(
    sum(
        line.strip() in valid(rules['0'])
        for line
        in open('input')
    )
)

