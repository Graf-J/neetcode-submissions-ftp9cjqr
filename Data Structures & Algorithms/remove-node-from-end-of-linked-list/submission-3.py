# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy, right = ListNode(0, next=head), head
        while n > 0:
            right = right.next
            n -= 1

        left = dummy
        while right:
            right = right.next
            left = left.next

        left.next = left.next.next
        return dummy.next
