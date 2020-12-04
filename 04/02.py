import re

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


def valid(pas):
    return bool(
        1920 <= int(pas['byr']) <= 2002 and
        2010 <= int(pas['iyr']) <= 2020 <= int(pas['eyr']) <= 2030 and
        re.fullmatch(r'[0-9]{2,3}(cm|in)', pas['hgt']) and
        (
            (pas['hgt'][-2:] == 'cm' and 150 <= int(pas['hgt'][:-2]) <= 193) or
            (pas['hgt'][-2:] == 'in' and 59 <= int(pas['hgt'][:-2]) <= 79)
        ) and
        re.fullmatch(r'#[0-9a-f]{6}', pas['hcl']) and
        pas['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'} and
        re.fullmatch(r'[0-9]{9}', pas['pid'])
    )


print(
    sum(
        all(r in pas for r in required) and valid(pas)
        for pas
        in passports
    )
)
