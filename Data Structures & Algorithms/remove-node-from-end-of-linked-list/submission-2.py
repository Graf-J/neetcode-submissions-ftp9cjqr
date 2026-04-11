# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy, current = ListNode(0, next=head), head
        while n > 0:
            current = current.next
            n -= 1

        walker = dummy
        while current:
            current = current.next
            walker = walker.next

        walker.next = walker.next.next
        return dummy.next
