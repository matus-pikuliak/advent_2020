from functools import cache
from itertools import product, islice

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


j = 0
for line in open('input').read().splitlines():
    c = ''.join(
        str(int(line[i:i+8] in valid(rules['42'])))
        for i
        in range(0, len(line), 8)
    )
    if '10' in c and '01' not in c and c.count('1') > c.count('0'):
        j += 1

print(j)
