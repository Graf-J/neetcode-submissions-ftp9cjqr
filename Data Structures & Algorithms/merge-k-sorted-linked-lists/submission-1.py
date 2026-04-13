import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other: NodeWrapper) -> bool:
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Fill Heap with first Nodes
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, NodeWrapper(node))

        # Do until Heap is empty
        dummy = ListNode()
        current = dummy
        while heap:
            node = heapq.heappop(heap).node
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, NodeWrapper(node.next))

        return dummy.next
        