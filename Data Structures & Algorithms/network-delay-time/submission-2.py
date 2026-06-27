class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))

        min_heap = [(0, k)]
        visited = set()
        max_distance = 0
        while min_heap:
            cur_t, node = heapq.heappop(min_heap)
            if node in visited:
                continue

            max_distance = max(max_distance, cur_t)
            visited.add(node)

            for neighbor, dist in adj[node]:
                heapq.heappush(min_heap, (cur_t + dist, neighbor))

        return max_distance if len(visited) == n else -1     