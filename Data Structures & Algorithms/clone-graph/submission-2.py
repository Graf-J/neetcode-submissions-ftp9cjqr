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

        node_map = {node: Node(val=node.val)}
        stack = [node]
        while stack:
            current = stack.pop()
            current_clone = node_map[current]
            for neighbor in current.neighbors:
                if neighbor in node_map:
                    current_clone.neighbors.append(node_map[neighbor])
                else:
                    node_map[neighbor] = Node(val=neighbor.val)
                    current_clone.neighbors.append(node_map[neighbor])
                    stack.append(neighbor)

        return node_map[node]
        