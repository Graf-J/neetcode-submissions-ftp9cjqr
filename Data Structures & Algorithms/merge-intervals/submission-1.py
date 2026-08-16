class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        start, end = 0, 1
        intervals.sort()
        result = []
        for i in range(1, len(intervals)):
            if intervals[i - 1][end] < intervals[i][start]:
                result.append(intervals[i - 1])
            else:
                intervals[i] = [
                    intervals[i - 1][start], 
                    max(intervals[i - 1][end], intervals[i][end])
                ]
        result.append(intervals[-1])
        return result
            