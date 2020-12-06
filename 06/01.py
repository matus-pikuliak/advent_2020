print(
    sum(
        len(set(c for c in group).difference('\n'))
        for group
        in open('input').read().split('\n\n')
    )
)
