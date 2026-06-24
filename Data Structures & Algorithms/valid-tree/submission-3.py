class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        ctr = 0
        visited = set()
        q = deque([(0, -1)])
        while q:
            node, parent = q.popleft()
            if node in visited:
                return False

            visited.add(node)
            ctr += 1

            for neighbor in adj[node]:
                if neighbor == parent:
                    continue

                q.append((neighbor, node))

        return ctr == n


# adj = [
#     0: [1, 2, 3],
#     1: [0, 4],
#     2: [0],
#     3: [0]
#     4: [1]
# ]
# ctr = 0
# visited = {}
# q = {(0, -1)}

# parent = 






