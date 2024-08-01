# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        decimal_value = 0
        current = head
        
        while current:
            decimal_value = (decimal_value << 1) | current.val
            current = current.next
        
        return decimal_value
