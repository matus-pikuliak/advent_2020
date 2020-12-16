import re
from math import prod

ranges = [
    tuple(map(int, re.findall('[0-9]+', line)))
    for line
    in open('input')
    if '-' in line
]

tickets = [
    list(map(int, line.split(',')))
    for line
    in open('input')
    if ',' in line
]

valid_tickets = [
    ticket
    for ticket
    in tickets
    if all(
        any(a <= v <= b or c <= v <= d for a, b, c, d in ranges)
        for v
        in ticket
    )
]

valid_columns = {
    (a, b, c, d): set(
        i
        for i
        in range(20)
        if all(a <= ticket[i] <= b or c <= ticket[i] <= d for ticket in valid_tickets)
    )
    for a, b, c, d
    in ranges
}

valid_ranges = {
    col: set(
        r
        for r, cols
        in valid_columns.items()
        if col in cols
    )
    for col
    in range(20)
}

print(
    prod(
        valid_tickets[0][col]
        for col, rs
        in valid_ranges.items()
        if len(rs) in set(21 - len(valid_columns[r]) for r in ranges[:6])
    )
)
