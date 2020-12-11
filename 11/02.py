from functools import cache

seats = {
    i + j*1j: False
    for i, line in enumerate(open('input').read().splitlines())
    for j, c in enumerate(line)
    if c == 'L'
}


@cache
def neighbors(seat):
    ns = []
    for d in [-1 - 1j, -1j, 1 - 1j, -1, 1, -1 + 1j, 1j, 1 + 1j]:
        for i in range(1, 100):
            if seat + d * i in seats:
                ns.append(seat + d * i)
                break
    return ns


def occ(seat):
    return sum(seats[n] for n in neighbors(seat))


while True:
    new_seats = {
        s: occ(s) == 0 or (occ(s) < 5 and o)
        for s, o
        in seats.items()
    }
    if new_seats == seats:
        print(sum(seats.values()))
        break
    seats = new_seats

