class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = 0, 1
        result = []
        for i in range(len(intervals)):
            if intervals[i][start] > newInterval[end]:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[start] > intervals[i][end]:
                result.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[start], intervals[i][start]),
                    max(newInterval[end], intervals[i][end])
                ]
            
        result.append(newInterval)
        return result
