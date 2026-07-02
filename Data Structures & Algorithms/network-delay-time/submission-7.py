class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v, t in times:
            adj[u].append((v, t))

        result = 0
        visited = set()
        min_heap = [(0, k)]
        while min_heap:
            dist, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            result = max(result, dist)
            for n_node, edge_weight in adj[node]:
                if n_node not in visited:
                    heapq.heappush(min_heap, (dist + edge_weight, n_node))

        return result if len(visited) == n else -1