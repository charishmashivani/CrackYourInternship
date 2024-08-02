#Day 16

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root, subRoot):
        # Helper function to check if two trees are identical
        def isSameTree(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            return (s.val == t.val) and isSameTree(s.left, t.left) and isSameTree(s.right, t.right)
        
        # Base case: if root is None, then subRoot cannot be a subtree
        if not root:
            return False
        
        # Check if the current tree (root) is identical to subRoot
        if isSameTree(root, subRoot):
            return True
        
        # Recursively check the left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        
