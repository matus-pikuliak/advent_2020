from itertools import combinations

nums = list(map(int, open('input')))
target = 14144619
target_id = 505

for lo, hi in combinations(range(target_id), 2):
    if sum(r := nums[lo:hi]) == target:
        print(max(r) + min(r))
        break
