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

class Solution(object):
    def rangeSumBST(self, root, low, high):
        def dfs(node):
            if not node:
                return 0
            
            total_sum = 0
            if low <= node.val <= high:
                total_sum += node.val
            
            if node.val > low:
                total_sum += dfs(node.left)
            
            if node.val < high:
                total_sum += dfs(node.right)
            
            return total_sum
        return dfs(root)

        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        
