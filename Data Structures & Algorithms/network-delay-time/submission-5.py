class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf") for _ in range(n)]
        dist[k - 1] = 0
        for _ in range(n - 1):
            for u, v, t in times:
                if dist[u - 1] + t < dist[v - 1]:
                    dist[v - 1] = dist[u - 1] + t

        max_time = max(dist)
        return max_time if max_time != float("inf") else -1