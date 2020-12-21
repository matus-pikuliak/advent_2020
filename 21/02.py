ingredients, allergens = list(), list()

for line in open('input'):
    ing, al = line[:-2].split('(contains')
    ingredients.append(set(ing.split()))
    allergens.append(set(al.split(',')))

maybe = {
    allergen: set.intersection(*(
        ing
        for ing, al
        in zip(ingredients, allergens)
        if allergen in al
    ))
    for allergen
    in set.union(*allergens)
}

definitely = {}
while maybe:
    for al, ing in maybe.items():
        ing -= set(definitely.values())
        if len(ing) == 1:
            definitely[al] = list(ing)[0]
            del maybe[al]
            break

print(','.join(definitely[k] for k in sorted(definitely)))

