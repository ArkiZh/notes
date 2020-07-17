"""
The n-queens puzzle is the problem of placing n queens on an n¡Án chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""

class Solution:
    def solveNQueens(self, n):
        if n<1:
            return []
        self.retval = []
        self._dfs(0,[],[],[],n)
        return [["."*val[i]+"Q"+"."*(n-1-val[i])  for i in range(n)] for val in self.retval]

    def _dfs(self, level, occupied_columns, black_sum, black_diff, n):
        if level==n:
            self.retval.append(occupied_columns.copy())
            return
        for i in range(n):
            if i not in occupied_columns and i+level not in black_sum and i-level not in black_diff:
                occupied_columns.append(i)
                black_sum.append(i+level)
                black_diff.append(i-level)
                self._dfs(level+1, occupied_columns, black_sum, black_diff, n)
                occupied_columns.pop()
                black_sum.pop()
                black_diff.pop()

import collections
class Solution1:
    def solveNQueens(self, n):
        if n<1:
            return []
        retval = []
        q = collections.deque()
        q.append((0, []))
        while q:
            cur_level, cur_used = q.popleft()

            if cur_level==n:
                retval.append(cur_used)

            # Find candidates in this level
            for i in range(n):
                if i in cur_used:
                    continue
                if cur_level+i in {x+cur_used[x] for x in range(len(cur_used))}:
                    continue
                if cur_level-i in {x-cur_used[x] for x in range(len(cur_used))}:
                    continue
                q.append((cur_level+1, cur_used+[i]))
        return [[ "."*col+"Q"+"."*(n-1-col) for col in val] for val in retval]
            
                    
                


                
for x in Solution1().solveNQueens(6):
    print("="*10)
    for xx in x:
        print(xx)
