class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heapq.heappush_max(heap, (x**2 + y**2, x, y))
            if len(heap) > k:
                heapq.heappop_max(heap)

        return [[x, y] for _, x, y in heap]