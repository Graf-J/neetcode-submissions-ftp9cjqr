class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # Adj. stores all connections (square) after going through this nested loop
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                (x1, y1), (x2, y2) = points[i], points[j]
                d = abs(x2 - x1) + abs(y2 - y1)
                adj[i].append((j, d))
                adj[j].append((i, d))

        total_cost = 0
        visited = set()
        min_heap = [(0, 0)]
        while len(visited) < n:
            dist, node = heapq.heappop(min_heap)
            if node in visited: # Very similar dynamics like in Dijkstra (heap can contain duplicates)
                continue
            visited.add(node)
            total_cost += dist
            for neighbor, w in adj[node]:
                if neighbor not in visited: # Optimization like in Dijkstra
                    heapq.heappush(min_heap, (w, neighbor)) # Here don't do dist + w but just w instead (current frontier)
        
        return total_cost