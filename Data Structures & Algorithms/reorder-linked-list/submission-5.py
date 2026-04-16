# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find Left-Biased Center 
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        # Reverse Second Half
        prev, current = None, slow.next
        slow.next = None
        while current:
            tmp = current.next
            current.next = prev
            prev, current = current, tmp

        # Connect two Lists
        list1, list2 = head, prev
        while list2:
            tmp1, tmp2 = list1.next, list2.next
            list1.next = list2
            list2.next = tmp1
            list1, list2 = tmp1, tmp2



