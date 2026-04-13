# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        result_dummy = ListNode()
        result = result_dummy
        current = head
        while current:
            prev = None
            group_start = current
            ctr = 1
            while current and ctr <= k:
                tmp = current.next
                current.next = prev
                prev = current
                current = tmp
                ctr += 1

            if ctr == k + 1:
                result_dummy.next = prev
                result_dummy = group_start
            else:
                current, prev = prev, None
                while current:
                    tmp = current.next
                    current.next = prev
                    prev = current
                    current = tmp
                result_dummy.next = prev

        return result.next
