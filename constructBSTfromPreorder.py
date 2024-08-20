#Day 31

class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

def Bst(pre, size):
    def constructBST(pre, n, mini, maxi):
        nonlocal index
        if index >= n:
            return None

        if pre[index] < mini or pre[index] > maxi:
            return None

        root = Node(pre[index])
        index += 1

        root.left = constructBST(pre, n, mini, root.data)

        root.right = constructBST(pre, n, root.data, maxi)

        return root

    index = 0
    root = constructBST(pre, size, float('-inf'), float('inf'))
    
    return root

def postorderTraversal(root):
    if root is None:
        return
    
    postorderTraversal(root.left)
    postorderTraversal(root.right)
    print(root.data, end=" ")
