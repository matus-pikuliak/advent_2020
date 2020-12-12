dirs = {'E': 1j, 'S': 1, 'W': -1j, 'N': -1}
rot = {'R': 1, 'L': -1}

pos, wp = 0, -1 + 10j


def rot_right(point, num):
    if num == 0:
        return point
    point = point.imag - point.real * 1j
    return rot_right(point, num - 1)


for line in open('input'):
    c, num = line[0], int(line[1:])
    wp += dirs.get(c, 0) * num
    if c == 'F':
        pos += wp * num
    wp = rot_right(wp, (rot.get(c, 0) * num // 90) % 4)

print(abs(int(pos.imag)) + abs(int(pos.real)))

