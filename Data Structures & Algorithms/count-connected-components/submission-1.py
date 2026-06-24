class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(node):
            stack = [node]
            visited.add(node)
            while stack:
                current = stack.pop()
                for neighbor in adj[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

        num_components = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                num_components += 1

        return num_components
                