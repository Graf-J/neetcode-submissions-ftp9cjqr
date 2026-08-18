class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        last_end = intervals[0][1]
        num_removed = 0

        for i in range(1, len(intervals)):
            if last_end > intervals[i][0]:
                num_removed += 1
                last_end = min(last_end, intervals[i][1])
            else:
                last_end = intervals[i][1]

        return num_removed




# [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4]]

# [[1, 100], [2, 3], [4, 5]]



