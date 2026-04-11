# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy, carry = ListNode(0), 0
        result = dummy
        while l1 and l2:
            dummy.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10
            l1, l2, dummy = l1.next, l2.next, dummy.next

        tail = l1 or l2
        while tail:
            dummy.next = ListNode((tail.val + carry) % 10)
            carry = (tail.val + carry) // 10
            tail, dummy = tail.next, dummy.next

        if carry:
            dummy.next = ListNode(1)

        return result.next



        # Temp capturing overflow
        # Loop while both lists have values

        # Carry Temp on for remaining List

        # If Temp is 1, create one last node