class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build n x n Matrix
        dist = [[float("inf")] * n for _ in range(n)]
        # Set Diagonal = 0
        for i in range(n):
            dist[i][i] = 0
        # Set edges
        for src, dst, t in times:
            dist[src - 1][dst - 1] = t

        # Core Algorithm (Matrix Update)
        for i in range(n):
            for src in range(n):
                for dst in range(n):
                    if dist[src][i] + dist[i][dst] < dist[src][dst]:
                        dist[src][dst] = dist[src][i] + dist[i][dst]

        # Find max. Distance from k
        max_dist = max(dist[k - 1])
        return -1 if max_dist == float("inf") else max_dist

        
