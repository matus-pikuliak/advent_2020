from functools import reduce

print(
    sum(
        len(reduce(
            set.intersection,
            map(set, group.split())
        ))
        for group
        in open('input').read().split('\n\n')
    )
)
