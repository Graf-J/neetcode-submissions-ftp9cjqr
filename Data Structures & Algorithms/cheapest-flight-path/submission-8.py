class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float("inf")] * n
        dist[src] = 0
        for _ in range(k + 1):
            dist_tmp = dist.copy()
            for s, d, p in flights:
                if dist[s] + p < dist_tmp[d]:
                    dist_tmp[d] = dist[s] + p

            dist = dist_tmp

        return -1 if dist[dst] == float("inf") else dist[dst]
