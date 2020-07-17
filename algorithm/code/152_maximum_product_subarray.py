"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

class Solution:
    def maxProduct(self, nums):
        if nums is None or len(nums)==0: return None
        dp = [nums[0],nums[0]] # max, min of current index
        retval = dp[0]
        for i in range(1, len(nums)):
            candidates = [dp[0]*nums[i], dp[1]*nums[i], nums[i]]
            cur_max, cur_min = max(candidates), min(candidates)
            retval=max(retval,cur_max)
            dp = [cur_max, cur_min]
        return retval





nums = [2,3,-2,4]
print(Solution().maxProduct(nums))
