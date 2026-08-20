class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        num_remove = 0
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:
                prev_end = min(prev_end, intervals[i][1])
                num_remove += 1
            else:
                prev_end = intervals[i][1]

        return num_remove
            



# |----|
#      |---------|
# |--------------|


# |----|
# |--------------|
#      |---------|