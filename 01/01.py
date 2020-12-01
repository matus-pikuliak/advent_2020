expenses = set(
    int(line)
    for line
    in open('input')
)

for e1 in expenses:
    if (e2 := 2020 - e1) in expenses:
        print(e1 * e2)
        break