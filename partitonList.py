#Day 17

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head, x):
        less_head = ListNode(0)
        greater_head = ListNode(0)
        
        less = less_head
        greater = greater_head
        
        current = head
        while current:
            if current.val < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next
        
        greater.next = None
        
        less.next = greater_head.next
        
        return less_head.next

        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
