# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = head
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        current = slow.next
        slow.next = None
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        tail = prev

        while tail:
            dummy_temp, tail_temp = dummy.next, tail.next
            dummy.next = tail
            tail.next = dummy_temp
            dummy, tail = dummy_temp, tail_temp


# head
# (2) -> (4) -> (6) -> None

# tail
# (10) -> (8) -> None


# head
# (2) -> (4) -> None

# tail
# (10) -> (8) -> None