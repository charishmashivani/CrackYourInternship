#Day 32

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        # Start flattening from the root
        self.flatten(root.left)
        self.flatten(root.right)
        
        # Store the right subtree
        right_subtree = root.right
        
        # Move the left subtree to the right
        root.right = root.left
        root.left = None
        
        # Traverse to the end of the new right subtree
        current = root
        while current.right:
            current = current.right
        
        # Attach the originally right subtree
        current.right = right_subtree
