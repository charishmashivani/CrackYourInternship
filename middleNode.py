#Day 3

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        first = head
        second = head

        while second is not None and second.next is not None:
            first = first.next
            second = second.next.next
        
        return first

        """
        :type head: ListNode
        :rtype: ListNode
        """
        
