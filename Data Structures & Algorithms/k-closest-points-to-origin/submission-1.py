class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(x**2 + y**2, i) for i, (x, y) in enumerate(points)]
        heapq.heapify(distances)

        result = []
        for _ in range(k):
            i = heapq.heappop(distances)[1]
            result.append(points[i])

        return result