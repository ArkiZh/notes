"""

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    
    def twoSum(self, nums, target):
        # 这个方法有漏洞，对于重复值没法处理
        d = dict()
        for i, v in enumerate(nums):
            d[v]=i
        print(d)
        for i, v in enumerate(nums):
            j = d.get(target-v)
            if j is not None and j != i:
                return i,j
        return None

    def twoSum1(self, nums, target):
        d = dict()
        for i, v in enumerate(nums):
            j = d.get(target-v)
            if j is not None:
                return i, j
            d[v]=i
        return None
    

print(Solution().twoSum1(list(range(10)),12))
