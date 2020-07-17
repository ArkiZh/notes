"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        retval = []
        def dfs(cur,level):
            if cur is None:
                return
            if len(retval)-1<level:
                retval.append([cur])
            else:
                retval[level].append(cur)

            dfs(cur.left, level+1)
            dfs(cur.right, level+1)
        dfs(root,0)
        return retval


from queue import deque
class Solution1:
    def levelOrder(self, root):
        retval = []
        q = deque()
        q.append((0,root))
        while q:
            level, cur = q.popleft()
            if cur is None:
                continue
            if len(retval)-1 <level:
                retval.append([cur.val])
            else:
                retval[level].append(cur.val)
            q.append((level+1, cur.left))
            q.append((level+1, cur.right))
        return retval


class Solution2:
    def levelOrder(self, root):
        if root is None:
            return []
        retval = []
        q = deque()
        q.append((0,root))
        while q:
            level, cur = q.pop()
            if len(retval)-1 < level:
                retval.append([cur.val])
            else:
                retval[level].append(cur.val)

            if cur.right:
                q.append((level+1,cur.right))
            if cur.left:
                q.append((level+1,cur.left))
        return retval


import collections
class Solution3:
    def levelOrder(self, root):
        if root is None:
            return []
        retval = []
        q = collections.deque()
        q.append(root)

        # visited = set()
        
        while q:
            level_size = len(q)
            cur_level = []
            for i in range(level_size):
                cur = q.popleft()
                cur_level.append(cur.val)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            retval.append(cur_level)
        return retval
                
                
class Solution4:
    def levelOrder(self, root):
        if root is None:
            return []
        retval = []
        def dfs(cur, level):
            if cur is None:
                return
            if len(retval)-1 <level:
                retval.append([])
            retval[level].append(cur.val)
            dfs(cur.left, level+1)
            dfs(cur.right, level+1)
        dfs(root, 0)
        return retval
