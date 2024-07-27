#Day 10

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half_start = self.reverseList(slow)

        first_half_start = head
        second_half_copy = second_half_start
        
        is_palindrome = True
        while second_half_start:
            if first_half_start.val != second_half_start.val:
                is_palindrome = False
                break
            first_half_start = first_half_start.next
            second_half_start = second_half_start.next

        self.reverseList(second_half_copy)
        
        return is_palindrome

def create_linked_list(vals):
    head = ListNode(vals[0])
    current = head
    for val in vals[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
