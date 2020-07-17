"""
Given an array of size n, find the majority element. The majority element is the element that appears more than  n/2 times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""

class Solution:
    def majorityElement(self, nums):
        if nums is None:
            return None
        t = len(nums)/2
        d = dict()
        for num in nums:
            c = d.get(num)
            c = 1 if c is None else c+1
            if c>t:
                return num
            d[num] = c
        return None

class Solution1:
    def majorityElement(self, nums):
        def find_sub_majority(low, high):
            if low==high:
                return nums[low]

            mid = (low+high)//2

            left = find_sub_majority(low,mid)
            right = find_sub_majority(mid+1, high)

            if left == right:
                return left

            left_count, right_count = 0, 0

            for i in range(low,high+1):
                if left==nums[i]:
                    left_count+=1
                elif right==nums[i]:
                    right_count+=1
            return left if left_count>right_count else right
        return find_sub_majority(0,len(nums)-1)

    
class Solution2:
    def majorityElement(self, nums):
        candidate = 0
        count = 0
        for x in nums:
            if count==0:
                candidate = x
            count+=1 if candidate==x else -1

        return candidate
                
            
