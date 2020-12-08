lines = [
    (line.split()[0], int(line.split()[1]))
    for line
    in open('input').read().splitlines()
]

pos = acc = 0
visited = set()
while pos not in visited:
    visited.add(pos)
    instr, attr = lines[pos]

    pos += attr if instr == 'jmp' else 1
    acc += instr == 'acc' and attr

print(acc)