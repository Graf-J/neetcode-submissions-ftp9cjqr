class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, t in times:
            adj[u - 1].append((v - 1, t))

        min_heap = [(0, k - 1)]
        visited = set()
        last_time = 0
        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in visited:
                continue

            visited.add(node)
            last_time = time
            for neighbor, weight in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (time + weight, neighbor))

        return last_time if len(visited) == n else -1
        