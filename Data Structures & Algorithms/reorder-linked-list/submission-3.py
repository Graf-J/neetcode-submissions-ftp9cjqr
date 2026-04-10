# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find (left-biased) Middle of List
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right_center = slow.next
        slow.next = None

        # Reverse second half of List
        prev = None
        while right_center:
            tmp = right_center.next
            right_center.next = prev
            prev = right_center
            right_center = tmp

        # Merge to final reordered List
        list1, list2 = head, prev
        while list2:
            tmp_list1 = list1.next
            tmp_list2 = list2.next
            list1.next = list2
            list2.next = tmp_list1
            list1, list2 = tmp_list1, tmp_list2


# 1, 2, 3, 4
# 1, 2
# 3, 4
# 4, 3
# 1, 4, 2, 3

# 1, 2, 3, 4, 5
# 1, 2
# 3, 4, 5
# 5, 4, 3
# 1, 5, 2, 4, 3


