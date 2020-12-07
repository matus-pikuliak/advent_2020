from collections import defaultdict

bags = defaultdict(set)

for line in open('input'):
    words = line.split()
    for i in range(5, len(words), 4):
        bags[words[i] + words[i+1]].add(words[0] + words[1])

al = set(bags['shinygold'])
while len(al) != len(al := al | set.union(*[bags[bag] for bag in al])): pass
print(len(al))

