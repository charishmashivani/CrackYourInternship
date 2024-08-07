#Day 21

class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        def flatten_rec(node):
            current = node
            last = None
            
            while current:
                if current.child:
                    child_last = flatten_rec(current.child)
                    
                    next_node = current.next
                    current.next = current.child
                    current.child.prev = current
                    current.child = None
                    
                    if child_last:
                        child_last.next = next_node
                    if next_node:
                        next_node.prev = child_last
                    
                    last = child_last
                else:
                    last = current
                
                current = current.next
            
            return last
        
        flatten_rec(head)
        
        return head
