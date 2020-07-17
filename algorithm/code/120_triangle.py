"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

"""


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        h = len(triangle)
        if h<=1:
            return triangle[0][0]
        memo = [0]*(h+1)
        for i in range(h)[::-1]:
            cur = triangle[i]
            for j in range(len(cur)):
                memo[j] = cur[j]+min(memo[j:j+2])
        return memo[0]
