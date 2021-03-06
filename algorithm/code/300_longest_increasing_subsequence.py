"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""

class Solution:
    def lengthOfLIS(self, nums):
        if nums==None or len(nums)==0:
            return 0
        dp = [1]*len(nums)
        retval = 1
        for i in range(1, len(nums)):
            cur = 1
            for j in range(i):
                if nums[j]<nums[i] and dp[j]+1>cur:
                       cur = dp[j]+1
            dp[i] = cur
            if cur>retval:
                retval=cur
        return retval
    

print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
