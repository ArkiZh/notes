"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

"""

import math
class Solution:
    def numSquares(self, n):
        if n<=1:
            return 1
        steps = [x**2 for x in range(1, int(math.sqrt(n))+1)]
        dp = [0]*(n+1)
        for i in range(1,n+1):
            cur_min = float("inf")
            for j in steps:
                if i-j>=0:
                    if dp[i-j]<cur_min:
                        cur_min=dp[i-j]
                else:
                    break
            dp[i]=cur_min+1
        return dp[-1]

    def numSquares1(self, n):
        if n<=1:
            return 1
        steps = [x**2 for x in range(1, int(math.sqrt(n))+1)]
        dp = [float("inf")]*(n+1)
        dp[0]=0
        for i in range(n):
            for s in steps:
                if i+s<=n:
                    if dp[i]+1<dp[i+s]:
                        dp[i+s]=dp[i]+1
                else:
                    break
        return dp[-1]

    def numSquares2(self, n):
        if n<=1:
            return 1
        steps = [x**2 for x in range(1, int(math.sqrt(n))+1)]
        cnt = 0
        cur_level = [0]
        visited = set()
        while cur_level:
            cnt+=1
            next_level = []
            for cur in cur_level:
                for s in steps:
                    if cur+s==n:
                        return cnt
                    if cur+s<n:
                        if cur+s not in visited:
                            next_level.append(cur+s)
                            visited.add(cur+s)
                    else:
                        break
            cur_level = next_level
            print(cnt, cur_level)
        return -1
            


    
print(Solution().numSquares(13))
print(Solution().numSquares1(13))
print(Solution().numSquares2(13))
