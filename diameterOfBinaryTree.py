#Day 14

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0
        
        def depth(node):
            """
            Compute the depth of a node and update the diameter.
            """
            if not node:
                return 0
            
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            
            self.diameter = max(self.diameter, left_depth + right_depth)
            
            return max(left_depth, right_depth) + 1
        
        depth(root)
        return self.diameter
