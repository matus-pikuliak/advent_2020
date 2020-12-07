def cost(bag):
    return 1 + sum(
        num * cost(name) if name in bags else 1
        for num, name
        in bags[bag]
    )


bags = {
    words[0] + words[1]: [
        (int(words[i]), words[i+1] + words[i+2])
        for i
        in range(4, len(words), 4)
        if words[i] != 'no'
    ]
    for words
    in [line.split() for line in open('input')]
}

print(cost('shinygold') - 1)
