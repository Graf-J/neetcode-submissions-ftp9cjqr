class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for i, (x, y) in enumerate(points):
            heapq.heappush_max(max_heap, (x**2 + y**2, i))
            if len(max_heap) > k:
                heapq.heappop_max(max_heap)

        return [points[i] for _, i in max_heap]