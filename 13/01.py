lines = open('input').read().splitlines()
time = int(lines[0])
buses = [int(bus) for bus in lines[1].split(',') if bus != 'x']


def t(bus): return time - (time % bus) + bus


b = min(buses, key=t)
print((t(b) - time) * b)

