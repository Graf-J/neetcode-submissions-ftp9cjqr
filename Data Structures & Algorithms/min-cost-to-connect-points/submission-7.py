class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                (x1, y1), (x2, y2) = points[i], points[j]
                dist = abs(x2 - x1) + abs(y2 - y1)
                adj[i].append((j, dist))
                adj[j].append((i, dist))

        total_cost = 0
        visited = set()
        min_heap = [(0, 0)]
        while len(visited) < n:
            dist, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            total_cost += dist
            for neighbor, w in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (w, neighbor))

        return total_cost




