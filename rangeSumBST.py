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
            # Base case: if the node is None, return 0
            if not node:
                return 0
            
            total_sum = 0
            if low <= node.val <= high:
                # If node's value is within the range, add it to the sum
                total_sum += node.val
            
            # If node's value is greater than low, traverse left subtree
            if node.val > low:
                total_sum += dfs(node.left)
            
            # If node's value is less than high, traverse right subtree
            if node.val < high:
                total_sum += dfs(node.right)
            
            return total_sum
        
        # Start the DFS traversal from the root
        return dfs(root)

        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        
