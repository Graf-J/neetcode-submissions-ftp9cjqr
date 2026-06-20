# Can also be solved using DSU Cycle-Detection

# Criterion for valid Tree:
# - Fully Connected
# - No Cycles

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(parent, node):
            if node in visited:
                return False

            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue

                valid = dfs(node, neighbor)
                if not valid:
                    return False

            return True

        if not dfs(-1, 0):
            return False

        return len(visited) == n

# n = 5
# adj = [
#     (0): [1, 2, 3]
#     (1): [0, 4]
#     (2): [0]
#     (3): [0]
#     (4): [1]
# ]

