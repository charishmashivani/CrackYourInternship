#Day 16

class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        
        # Step 1: Interweaving the original and copied nodes
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next
        
        # Step 2: Setting up the random pointers for the copied nodes
        curr = head
        while curr:
            copied_node = curr.next
            copied_node.random = curr.random.next if curr.random else None
            curr = copied_node.next
        
        # Step 3: Separating the original and copied lists
        curr = head
        dummy_head = Node(0)
        copy_curr = dummy_head
        
        while curr:
            copy_node = curr.next
            curr.next = copy_node.next
            copy_curr.next = copy_node
            copy_curr = copy_node
            curr = curr.next
        
        return dummy_head.next
