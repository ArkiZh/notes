"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""

class Solution:
    def generateParenthesis(self, n):
        if n<1: return []
        self.retval = []
        self._dfs(0,0,n,"")
        return self.retval
        
    def _dfs(self, left_used, right_used, n, cur):
        if right_used==n:
            self.retval.append(cur)
            return
        if left_used==right_used:
            self._dfs(left_used+1, right_used, n, cur+"(")
        else:
            if left_used<n:
                self._dfs(left_used+1, right_used, n, cur+"(")
                self._dfs(left_used, right_used+1, n, cur+")")
            else:
                self._dfs(left_used, n, n, cur+")"*(n-right_used))
                


class Solution1:
    def generateParenthesis(self, n):
        if n<1: return []
        self.retval = []
        self._dfs(0,0,n,"")
        return self.retval
    def _dfs(self, left_used, right_used, n, cur):
        if right_used==n:
            self.retval.append(cur)
            return
        if left_used<n:
            self._dfs(left_used+1, right_used, n, cur+"(")
        if right_used<left_used:
            self._dfs(left_used, right_used+1, n,  cur+")")


import collections            
class Solution2:
    def generateParenthesis(self, n):
        """ BFS """
        if n<1: return []
        retval = []
        q = collections.deque()
        q.append((0,0,""))
        while q:
            left_used, right_used, cur = q.popleft()
            if right_used == n:
                retval.append(cur)
                continue
            if left_used<n:
                q.append((left_used+1, right_used, cur+"("))
            if right_used<left_used:
                q.append((left_used, right_used+1, cur+")"))
        return retval

    def generateParenthesis1(self, n):
        """ BFS """
        if n<1: return []
        retval = []
        q = collections.deque()
        q.append((0,0,[]))
        while q:
            left_used, right_used, cur = q.popleft()
            if right_used == n:
                retval.append("".join(cur))
                continue
            if left_used<n:
                q.append((left_used+1, right_used, cur+["("]))
            if right_used<left_used:
                q.append((left_used, right_used+1, cur+[")"]))
        return retval
