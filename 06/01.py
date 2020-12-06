print(
    sum(
        len(set(group).difference('\n'))
        for group
        in open('input').read().split('\n\n')
    )
)
