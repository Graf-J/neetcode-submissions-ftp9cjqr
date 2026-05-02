class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_heap = []
        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            dist_heap.append((x ** 2 + y ** 2, x, y))
        heapq.heapify(dist_heap)

        result = []
        for _ in range(k):
            _, x, y = heapq.heappop(dist_heap)
            result.append([x, y])

        return result
