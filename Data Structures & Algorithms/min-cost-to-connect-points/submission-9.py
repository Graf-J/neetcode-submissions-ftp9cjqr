class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        dist = [float("inf")] * n
        visited = [False] * n

        result = 0
        node = 0
        for _ in range(n):
            next_node = -1
            visited[node] = True
            for i in range(n):
                if visited[i]:
                    continue

                (x1, y1), (x2, y2) = points[node], points[i]
                d = abs(x2 - x1) + abs(y2 - y1)
                dist[i] = min(dist[i], d)
                if next_node == -1 or dist[i] < dist[next_node]:
                    next_node = i
            
            if next_node != -1:
                result += dist[next_node]
                node = next_node

        return result
            
            







