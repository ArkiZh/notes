"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4

"""

class Solution:
    def maximalSquare(self, matrix):
        if matrix is None or len(matrix)==0 or len(matrix[0])==0:
            return 0
        retval = 0
        dp = [[0 for __ in range(len(matrix[0])+1)]for _ in range(len(matrix)+1)]
        for i in range(1,len(matrix)+1):
            for j in range(1,len(matrix[0])+1):
                if matrix[i-1][j-1]=="1":
                    dp[i][j] = min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j])+1
                    if dp[i][j]>retval:
                        retval=dp[i][j]
        return retval**2


    
print(Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
