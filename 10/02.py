from functools import cache

nums = set(map(int, open('input')))
nums.add(max(nums) + 3)


@cache
def c(i):
    if i == 0:
        return 1
    if i not in nums:
        return 0
    return c(i-1) + c(i-2) + c(i-3)


print(c(max(nums)))
