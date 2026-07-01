class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, t in times:
            adj[u - 1].append((v - 1, t))

        min_time = 0
        visited = set()
        min_heap = [(0, k - 1)]
        while min_heap:
            t, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            min_time = max(min_time, t)
            visited.add(node)
            for neighbor_node, edge_t in adj[node]:
                if neighbor_node not in visited:
                    heapq.heappush(min_heap, (t + edge_t, neighbor_node))

        return min_time if len(visited) == n else -1
