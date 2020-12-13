intervals = [
    (i, int(j))
    for i, j
    in enumerate(open('input').readlines()[1].split(','))
    if j != 'x'
]

start, step = 0, intervals[0][1]

for a, b in intervals[1:]:
    while (start + a) % b != 0:
        start += step
    step *= b

print(start)


