"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution:
    def threeSum(self, nums):
        if nums is None or len(nums)<3:
            return []
        s = len(nums)
        nums.sort()
        result = set()
        for i in range(s-2):
            a = nums[i]
            if a>0:
                break
            left, right = i+1, s-1
            while left<right:
                b, c = nums[left], nums[right]
                if a+b+c == 0:
                    result.add(tuple(sorted([a,b,c])))
                    while left<right and b==nums[left]:
                        left+=1
                    while left<right and c==nums[right]:
                        right-=1
                elif a+b+c > 0:
                    right-=1
                else:
                    left+=1
        return [list(x) for x in result]

    def threeSum1(self, nums):
        if nums is None or len(nums)<3:
            return []
        s = len(nums)
        nums.sort()
        result = []
        for i in range(s-2):
            a = nums[i]
            if a>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            left, right = i+1, s-1
            while left<right:
                b, c = nums[left], nums[right]
                if a+b+c == 0:
                    result.append([a,b,c])
                    while left<right and b==nums[left]:
                        left+=1
                    while left<right and c==nums[right]:
                        right-=1
                elif a+b+c > 0:
                    right-=1
                else:
                    left+=1
        return result

    def threeSum2(self,nums):
        if nums is None or len(nums)<3:
            return []
        nums.sort()
        result = set()
        for i,v in enumerate(nums[:-2]):
            if v>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            d = set()
            for x in nums[i+1:]:
                if x not in d:
                    d.add(-v-x)
                else:
                    result.add((v,-v-x,x))
        print(result)
        return list(map(list, result))

print("...")
nums_test = [-1, 0, 1, 2, -1, -4]
nums_test = [-2,0,1,1,2]
print(Solution().threeSum2(nums_test))


