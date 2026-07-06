class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        visited = [False] * n
        dist = [float("inf")] * n


        node = edge_ctr = result = 0
        while edge_ctr < n - 1:
            visited[node] = True
            next_node = -1
            for i in range(n):
                if visited[i]:
                    continue
                (x1, y1), (x2, y2) = points[node], points[i]
                d = abs(x2 - x1) + abs(y2 - y1)
                dist[i] = min(dist[i], d)
                if next_node == -1 or dist[next_node] > dist[i]:
                    next_node = i

            edge_ctr += 1
            result += dist[next_node]
            node = next_node

        return result
                
                