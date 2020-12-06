print(
    sum(
        len(set(group) - {'\n'})
        for group
        in open('input').read().split('\n\n')
    )
)
