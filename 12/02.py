dirs = {'E': 1j, 'S': 1, 'W': -1j, 'N': -1}
rot = {'R': 1, 'L': -1}

pos, wp = 0, -1 + 10jd

for line in open('input'):
    c, num = line[0], int(line[1:])
    wp += dirs.get(c, 0) * num
    if c == 'F':
        pos += wp * num
    wp *= 1j ** (-rot.get(c, 0) * num // 90)


print(abs(int(pos.imag)) + abs(int(pos.real)))

