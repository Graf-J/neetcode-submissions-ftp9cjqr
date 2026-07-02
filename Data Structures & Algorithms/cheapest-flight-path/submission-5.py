class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for s, d, price in flights:
            adj[s].append((d, price))

        dist = [[float("inf")] * (k + 2) for _ in range(n)]
        dist[src][0] = 0

        min_heap = [(0, src, -1)]        
        while min_heap:
            cost, node, stops = heapq.heappop(min_heap)
            if node == dst:
                return cost

            if cost > dist[node][stops + 1] or stops == k:
                continue

            dist[node][stops + 1] = cost
            for neighbor, edge_cost in adj[node]:
                if dist[neighbor][stops + 2] == float("inf"):
                    heapq.heappush(min_heap, (cost + edge_cost, neighbor, stops + 1))

        return -1

