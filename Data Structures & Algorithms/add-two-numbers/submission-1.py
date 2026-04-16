# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = result = ListNode()
        carry = 0

        # Add Up Lists
        while l1 and l2:
            value = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) >= 10
            result.next = ListNode(value)
            l1, l2, result = l1.next, l2.next, result.next

        # Add in longer List
        residuals = l1 or l2
        while residuals:
            value = (residuals.val + carry) % 10
            carry = (residuals.val + carry) == 10
            result.next = ListNode(value)
            residuals, result = residuals.next, result.next

        # Don't forget Carry
        if carry:
            result.next = ListNode(1)

        return dummy.next

