"""
https://leetcode.com/problems/two-sum/description/
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    result = []
    for idx, n in enumerate(nums):
        com = target - n
        if com in seen.keys():
            result.append(seen[com])
            result.append(idx)
        else:
            seen[n] = idx
    print(nums, result)
    return result

two_sum([2,7,11,15], 9)  # [0,1]
two_sum([3,2,4], 6)       # [1,2]
two_sum([3,3], 6)         # [0,1]



