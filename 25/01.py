card_key, door_key = map(int, open('input'))

acc = 1
loop = 0
while acc != card_key:
    loop += 1
    acc = acc * 7 % 20201227

print(pow(door_key, loop, 20201227))
