# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:   
    def get_min_idx(self, lists):
        min_idx, min_value = -1, float("inf")
        for i, node in enumerate(lists):
            if node is None:
                continue
            if node.val < min_value:
                min_value = node.val
                min_idx = i

        return min_idx
            
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        while any(node for node in lists):
            min_idx = self.get_min_idx(lists)
            current.next = lists[min_idx]
            current = current.next
            lists[min_idx] = lists[min_idx].next

        return dummy.next