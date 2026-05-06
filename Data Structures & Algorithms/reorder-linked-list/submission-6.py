# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        cur = slow.next
        slow.next = None
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev, cur = cur, tmp

        start, rev = head, prev
        while start and rev:
            start_tmp, rev_tmp = start.next, rev.next
            start.next = rev
            rev.next = start_tmp
            start, rev = start_tmp, rev_tmp


