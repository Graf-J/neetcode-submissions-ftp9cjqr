class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, t in times:
            adj[u - 1].append((v - 1, t))
        
        max_time = 0
        visited = set()
        min_heap = [(0, k - 1)]
        while min_heap:
            t, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            max_time = max(max_time, t)
            for neighbor, edge in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (t + edge, neighbor))

        return max_time if len(visited) == n else -1
