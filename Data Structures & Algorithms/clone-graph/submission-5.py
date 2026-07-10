"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_new_map = {}
        def dfs(old: Optional['Node']) -> Optional['Node']:
            if old is None:
                return None

            if old in old_new_map:
                return old_new_map[old]

            new = Node(old.val)
            old_new_map[old] = new
            for old_neighbor in old.neighbors:
                new_neighbor = dfs(old_neighbor)
                new.neighbors.append(new_neighbor)

            return new

        return dfs(node)