class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float("inf") for _ in range(n)]
        dist[src] = 0
        for _ in range(k + 1):
            dist_tmp = dist.copy()
            for s, d, p in flights: # s=from_i; d=to_i; p=price
                if dist[s] < float("inf") and dist[s] + p < dist_tmp[d]:
                    dist_tmp[d] = dist[s] + p
            dist = dist_tmp

        return dist[dst] if dist[dst] < float("inf") else -1