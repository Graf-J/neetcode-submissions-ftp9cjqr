class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float("inf")] * n
        dist[src] = 0
        for _ in range(k + 1):
            dist_copy = dist.copy()
            for from_i, to_i, price_i in flights:
                if dist[from_i] != float("inf") and dist[from_i] + price_i < dist_copy[to_i]:
                    dist_copy[to_i] = dist[from_i] + price_i

            dist = dist_copy

        return -1 if dist[dst] == float("inf") else dist[dst]