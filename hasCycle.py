# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        
        first = head
        second = head.next
        
        while second and second.next:
            if first == second:
                return True
            first = first.next
            second = second.next.next
        
        return False
