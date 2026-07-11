class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        result = 0
        visited = set()
        min_heap = [(0, 0)]
        while min_heap:
            cost, point_idx = heapq.heappop(min_heap)
            if point_idx in visited:
                continue
            visited.add(point_idx)
            result += cost
            for next_point_idx in range(len(points)):
                if next_point_idx in visited:
                    continue

                (x1, y1), (x2, y2) = points[point_idx], points[next_point_idx]
                d = abs(x2 - x1) + abs(y2 - y1)
                heapq.heappush(min_heap, (d, next_point_idx))

        return result
            







