seats = {
    i + j * 1j: False
    for i, line in enumerate(open('input').read().splitlines())
    for j, c in enumerate(line)
    if c == 'L'
}


def occ(seat):
    return sum(
        seats.get(seat + d, 0)
        for d
        in [-1-1j, -1j, 1-1j, -1, 1, -1+1j, 1j, 1+1j]
    )


while seats != (seats := {
        k: occ(k) == 0 or (occ(k) < 4 and v)
        for k, v
        in seats.items()
    }): pass

print(sum(seats.values()))
