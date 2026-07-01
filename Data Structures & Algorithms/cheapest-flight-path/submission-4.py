class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, cst in flights:
            adj[u].append((v, cst))

        dist = [[float("inf")] * (k + 2) for _ in range(n)]
        dist[src][0] = 0

        heap = [(0, src, 0)]  # cost, node, edges_used

        while heap:
            cost, node, edges = heapq.heappop(heap)

            if node == dst:
                return cost

            if edges == k + 1:
                continue
            if cost > dist[node][edges]:
                continue

            for nei, w in adj[node]:
                new_cost = cost + w
                new_edges = edges + 1
                if new_cost < dist[nei][new_edges]:
                    dist[nei][new_edges] = new_cost
                    heapq.heappush(heap, (new_cost, nei, new_edges))

        return -1
