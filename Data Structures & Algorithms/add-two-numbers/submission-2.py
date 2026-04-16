# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = result = ListNode()
        c = 0
        while l1 or l2 or c:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            value = (l1_val + l2_val + c) % 10
            c = (l1_val + l2_val + c) >= 10
            result.next = ListNode(value)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            result = result.next

        return dummy.next
