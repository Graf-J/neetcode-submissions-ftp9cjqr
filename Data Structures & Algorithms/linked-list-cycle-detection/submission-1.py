# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next or not head.next.next:
            return False
        
        tortoise = head.next
        hare = head.next.next
        while hare and hare.next:
            if tortoise == hare:
                return True

            tortoise = tortoise.next
            hare = hare.next.next

        return False
