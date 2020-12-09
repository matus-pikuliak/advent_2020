from itertools import combinations

nums = list(map(int, open('input')))

for i in range(25, len(nums)):
    if nums[i] not in map(sum, combinations(nums[i-25: i], 2)):
        print(nums[i])
        break