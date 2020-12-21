ingredients, allergens = list(), list()

for line in open('input'):
    ing, al = line[:-2].split('(contains')
    ingredients.append(set(ing.split()))
    allergens.append(set(al.split(',')))

valid = set.union(*(
    set.intersection(*(
        ing
        for ing, al
        in zip(ingredients, allergens)
        if allergen in al
    ))
    for allergen
    in set.union(*allergens)
))

print(
    sum(
        len(ing - valid)
        for ing
        in ingredients
    )
)
