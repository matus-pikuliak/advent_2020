import re

recs = [
    re.match(r'(.*)-(.*) (.*): (.*)', line).groups()
    for line
    in open('input')
]

print(
    sum(
        (pwd[int(lo)-1] == c) ^ (pwd[int(hi)-1] == c)
        for lo, hi, c, pwd
        in recs
    )
)