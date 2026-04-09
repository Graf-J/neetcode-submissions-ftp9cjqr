# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        l, r, ctr = 0, len(nodes) - 1, 0
        while l < r:
            if ctr % 2 == 0:
                nodes[l].next = nodes[r]
                l += 1
            else:
                nodes[r].next = nodes[l]
                r -= 1
            ctr += 1

        nodes[(l + r + 1) // 2].next = None
