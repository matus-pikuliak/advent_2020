from collections import Counter

nums = list(sorted(map(int, open('input'))))
nums = [0] + nums + [max(nums) + 3]

c = Counter(
    nums[i] - nums[i-1]
    for i
    in range(1, len(nums))
)

print(c[1] * c[3])
