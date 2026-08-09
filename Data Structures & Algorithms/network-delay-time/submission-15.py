class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, t in times:
            adj[u - 1].append((v - 1, t))

        max_time = 0
        num_visited = 0
        dist = [float("inf")] * n
        dist[k - 1] = 0
        
        heap = [(0, k - 1)]
        while heap:
            distance, node = heapq.heappop(heap)
            if distance != dist[node]:
                continue
            max_time = max(max_time, distance)
            num_visited += 1

            for neighbour, edge_weight in adj[node]:
                if distance + edge_weight < dist[neighbour]:
                    dist[neighbour] = distance + edge_weight
                    heapq.heappush(heap, (distance + edge_weight, neighbour))

        return max_time if num_visited == n else -1

