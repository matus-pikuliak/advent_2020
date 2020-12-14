import re
from itertools import product

memory = dict()
words = iter(re.sub(r'[^\w\s]', ' ', open('input').read()).split())

for word in words:
    if word == 'mask':
        mask = next(words)
        ones = int(mask.replace('X', '0'), 2)
        xs = [i for i, c in enumerate(mask) if c == 'X']
    else:
        adr = int(next(words)) | ones
        val = int(next(words))
        for vals in product([0, 1], repeat=len(xs)):
            for i, v in zip(xs, vals):
                if v:
                    adr |= 2 ** (35 - i)
                else:
                    adr &= ~ 2 ** (35 - i)
            memory[adr] = val

print(sum(memory.values()))
