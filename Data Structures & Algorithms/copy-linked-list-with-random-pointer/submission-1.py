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
        dummy = current = Node(0)
        while head:
            current.next = Node(head.val, next=None, random=head.random)
            old_new_map[head] = current.next
            head, current = head.next, current.next

        current = dummy.next
        while current:
            if current.random:
                current.random = old_new_map[current.random]
            current = current.next

        return dummy.next