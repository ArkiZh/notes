"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)

class Solution:
    def isValidBST(self, root):
                
        def valid_tree(r):
            if r is None:
                return True, None, None
            left_is, left_max, left_min = valid_tree(r.left)
            right_is, right_max, right_min = valid_tree(r.right)
            r_is = left_is and right_is and (r.val>left_max if left_max is not None else True) and (r.val<right_min if right_min is not None else True)
            return r_is, right_max if right_max is not None else r.val, left_min if left_min is not None else r.val
        return valid_tree(root)[0]

class Solution1:
    def isValidBST(self, root):
        # inorder traverse
        inorder_list = self.inorder(root)
        # check inorder list to be sorted
        for i in range(len(inorder_list)-1):
            if inorder_list[i] >= inorder_list[i+1]:
                return False
        return True
            

    def inorder(self, root):
        if root is None:
            return []
        left = self.inorder(root.left)
        right = self.inorder(root.right)
        return left+[root.val]+right

class Solution2:
    def isValidBST(self, root):
        self.prev = None
        return self.helper(root)

    def helper(self, root):
        print("==========> Deal root %s" % ("None" if not root else root.val))
        if root is None:
            print("Reach None")
            print("----------< Return True")
            return True
        print("Judge root.left")
        if not self.helper(root.left):
            print("----------< Return False")
            return False
        print("Judge prev>=root: %s >= %s"%(str("None" if not self.prev else self.prev.val), root.val))
        if self.prev and self.prev.val>=root.val:
            print("----------< Return False")            
            return False
        print("Give root to prev: %s -> %s"%(root.val, self.prev.val if self.prev else "None"))
        self.prev = root
        print("----------< Return right")
        return self.helper(root.right)

class Solution3:
    def isValidBST(self, root):
        return self.helper(root,None,None)

    def helper(self, root, min_node, max_node):
        if root is None:
            return True
        if min_node is not None and root.val<=min_node.val:
            return False
        if max_node is not None and root.val>=max_node.val:
            return False
        print(root, min_node, max_node)
        return self.helper(root.left,min_node, root) and self.helper(root.right, root, max_node)
            

if __name__=="__main__":
    root = TreeNode(100)
    root.left = TreeNode(50)
    root.left.left = TreeNode(25)
    root.left.right = TreeNode(75)
    root.right = TreeNode(150)
    root.right.left = TreeNode(125)
    root.right.right = TreeNode(175)

    # Solution2().isValidBST(root)
    print(Solution3().isValidBST(root))
