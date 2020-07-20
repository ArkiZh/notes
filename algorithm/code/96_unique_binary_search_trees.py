"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
 

Constraints:

1 <= n <= 19

"""

class Solution:
    def numTrees(self, n):
        if n<=0:
            return 0
        if n==1:
            return 1
        dp = [1]*(n+1)
        for i in range(2,n+1):
            dp[i] = sum([dp[j]*dp[i-j-1]for j in range(i)])
        return dp[-1]

print(Solution().numTrees(3))
