class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, t in times:
            adj[u - 1].append((v - 1, t))

        dist = [float("inf")] * n
        dist[k - 1] = 0
        min_heap = [(0, k - 1)]

        max_time = 0
        while min_heap:
            t, node = heapq.heappop(min_heap)
            if dist[node] != t:
                continue
            max_time = max(max_time, t)
            for neighbor, w in adj[node]:
                if t + w < dist[neighbor]:
                    dist[neighbor] = t + w
                    heapq.heappush(min_heap, (t + w, neighbor))

        return max_time if all(t < float("inf") for t in dist) else -1