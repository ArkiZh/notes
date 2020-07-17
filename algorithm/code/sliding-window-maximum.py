"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
"""
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums or k < 1 or k > len(nums):
            return None
        if k == 1:
            return nums
        retval = []
        q = deque([0], maxlen=k)

        def deal(ind):
            print([nums[_] for _ in q])
            if q[0] <= ind-k:
                q.popleft()
            while len(q) > 0 and nums[q[-1]] <= nums[ind]:
                q.pop()
            q.append(ind)

        for i in range(k-1):
            deal(i+1)
        retval.append(nums[q[0]])
        for i in range(len(nums)-k):
            deal(i+k)
            retval.append(nums[q[0]])
        return retval


class Solution1:
    def maxSlidingWindow(self, nums, k):
        if not nums or k < 1 or k > len(nums):
            return None
        if k == 1:
            return nums
        retval, q = [], deque(maxlen=k)
        for i, v in enumerate(nums):
            if len(q) > 0 and q[0] <= i-k:
                q.popleft()
            while len(q) > 0 and nums[q[-1]] <= v:
                q.pop()
            q.append(i)
            if i >= k-1:
                retval.append(nums[q[0]])
        return retval



print("==========")
# nums = [1,3,-1,-3,5,3,6,7]
# k = 3
# print(Solution().maxSlidingWindow(nums,k))

# nums = [7,2,4]
# k = 2
# print(Solution().maxSlidingWindow(nums,k))

nums = [1,3,1,2,0,5]
k = 3
# print(Solution().maxSlidingWindow(nums,k))
print(Solution1().maxSlidingWindow(nums,k))
