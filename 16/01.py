import re

ranges = [
    list(map(int, r.split('-')))
    for r
    in re.findall('[0-9]+-[0-9]+', open('input').read())
]

print(
    sum(
        int(ticket)
        for ticket
        in re.split('[\n,]', open('input').read().split('nearby tickets:\n')[1])
        if not any(r[0] <= int(ticket) <= r[1] for r in ranges)
    )
)
