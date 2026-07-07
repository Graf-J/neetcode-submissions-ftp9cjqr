class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        dist = [float("inf")] * n
        visited = [False] * n

        result = 0
        num_nodes = 1
        node = 0
        while num_nodes < n:
            visited[node] = True
            next_node = -1
            for i in range(n):
                if visited[i]:
                    continue
                (x1, y1), (x2, y2) = points[node], points[i]
                d = abs(x2 - x1) + abs(y2 - y1)
                dist[i] = min(dist[i], d)
                if next_node == -1 or dist[i] < dist[next_node]:
                    next_node = i
            
            result += dist[next_node]
            num_nodes += 1
            node = next_node

        return result
            
            



