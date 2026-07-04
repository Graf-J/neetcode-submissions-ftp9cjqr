class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf")] * n
        dist[k - 1] = 0
        for _ in range(n - 1):
            for u, v, t in times:
                if dist[u - 1] + t < dist[v - 1]:
                    dist[v - 1] = dist[u - 1] + t

        max_dist = max(dist)
        return -1 if max_dist == float("inf") else max_dist