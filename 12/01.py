dirs = {'E': 1j, 'S': 1, 'W': -1j, 'N': -1}
rot = {'R': 1, 'L': -1}

pos, dr = 0, 0

for line in open('input'):
    c, num = line[0], int(line[1:])
    pos += dirs.get(c, 0) * num
    if c == 'F':
        pos += list(dirs.values())[dr] * num
    dr = (dr + num * rot.get(c, 0) // 90) % 4


print(abs(int(pos.imag)) + abs(int(pos.real)))

