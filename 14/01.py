import re

memory = dict()
words = iter(re.sub(r'[^\w\s]', ' ', open('input').read()).split())

for word in words:
    if word == 'mask':
        mask = next(words)
        ones = int(mask.replace('X', '0'), 2)
        zeros = int(mask.replace('X', '1'), 2)
    else:
        memory.__setitem__(next(words), int(next(words)) | ones & zeros)

print(sum(memory.values()))
