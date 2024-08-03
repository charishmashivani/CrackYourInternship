#Day 17

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        
        def split_list(head):
            slow = head
            fast = head
            prev = None
            
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            
            prev.next = None
            return slow
        
        def merge_list(left, right):
            dummy = ListNode(0)
            tail = dummy
            
            while left and right:
                if left.val < right.val:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next
            
            if left:
                tail.next = left
            else:
                tail.next = right
            
            return dummy.next
        
        mid = split_list(head)
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(mid)
        
        return merge_list(left_sorted, right_sorted)

        """
        :type head: ListNode
        :rtype: ListNode
        """
        
