class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])

        heap = []
        result = {}
        i = 0
        for q in sorted(queries):
            # Add Intervals with valid Start
            while i < len(intervals) and intervals[i][0] <= q:
                interval_len = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(heap, (interval_len, intervals[i][1]))
                i += 1

            # Remove expired Intervals
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            result[q] = -1 if not heap else heap[0][0]

        return [result[q] for q in queries]
            
