import re

recs = [
    re.match(r'(.*)-(.*) (.*): (.*)', line).groups()
    for line
    in open('input')
]

print(
    sum(
        int(lo) <= pwd.count(c) <= int(hi)
        for lo, hi, c, pwd
        in recs
    )
)