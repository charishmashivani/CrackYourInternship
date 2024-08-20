#Day 31

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def constructTreeUtil(pre, preLN, n, index):
    if index[0] == n:
        return None
    
    node = Node(pre[index[0]])
    
    currIndex = index[0]
    
    index[0] += 1
    
    if preLN[currIndex] == 'N':
        node.left = constructTreeUtil(pre, preLN, n, index)
        node.right = constructTreeUtil(pre, preLN, n, index)
    
    return node

def constructTree(pre, preLN, n):
    index = [0]
    return constructTreeUtil(pre, preLN, n, index)

def printInorder(node):
    if node is None:
        return
    printInorder(node.left)
    print(node.data, end=' ')
    printInorder(node.right)
