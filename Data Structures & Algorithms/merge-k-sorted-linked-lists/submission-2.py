import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node: ListNode) -> None:
        self.node = node

    def __lt__(self, other: NodeWrapper) -> bool:
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, NodeWrapper(node))

        dummy = result = ListNode()
        while len(heap) > 0:
            smallest_node = heapq.heappop(heap)
            result.next = smallest_node.node
            result = result.next
            if smallest_node.node.next:
                heapq.heappush(heap, NodeWrapper(smallest_node.node.next))

        return dummy.next