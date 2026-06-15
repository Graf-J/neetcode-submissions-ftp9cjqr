"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        node_map = {}
        def dfs(old):
            if old in node_map:
                return node_map[old]

            new = Node(old.val)
            node_map[old] = new
            new.neighbors = [
                dfs(neighbor) for neighbor in old.neighbors
            ]
            return new

        return dfs(node)


