seats = {
    i + j*1j: False
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


while True:
    new_seats = {
        s: occ(s) == 0 or (occ(s) < 4 and o)
        for s, o
        in seats.items()
    }
    if new_seats == seats:
        print(sum(seats.values()))
        break
    seats = new_seats

