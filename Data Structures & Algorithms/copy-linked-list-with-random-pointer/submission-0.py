"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_new_map = {}
        new_dummy = Node(0)
        current, new_current = head, new_dummy
        while current:
            node = Node(current.val)
            new_current.next = node
            old_new_map[current] = node
            current, new_current = current.next, new_current.next

        current, new_current = head, new_dummy.next
        while current:
            if current.random is not None:
                new_current.random = old_new_map[current.random]
            current, new_current = current.next, new_current.next

        return new_dummy.next