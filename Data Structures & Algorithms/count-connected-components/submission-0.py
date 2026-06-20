# Can be solved using DSU

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for neighbor in adj[node]:
                dfs(neighbor)

        components = 0
        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)

        return components


# n = 5
# adj = {
#     0: [1]
#     1: [0, 2]
#     2: [1]
#     3: [4]
#     4: [3]
# }
# visited = {0, 1, 2, 3, 4}
# components = 2
# nodes = [0, 1, 2, <3>, 4]




