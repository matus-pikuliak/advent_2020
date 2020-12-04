# noinspection PyTypeChecker
passports = [
    dict(
        line.split(':')
        for line
        in pas.split()
    )
    for pas
    in open('input').read().split('\n\n')
]

required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

print(
    sum(
        all(r in pas for r in required)
        for pas
        in passports
    )
)
