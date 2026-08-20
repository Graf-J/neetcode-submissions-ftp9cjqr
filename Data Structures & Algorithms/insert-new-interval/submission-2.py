class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                result.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                result.append(newInterval)
                return result + intervals[i:]
            else:
                newInterval = [
                    min(intervals[i][0], newInterval[0]),
                    max(intervals[i][1], newInterval[1])
                ]

        result.append(newInterval)
        return result




# 1) Keep newInterval
# |------|
#           |------|

# 2) Return
#           |------|
# |------|

# 3) Update newInterval
#     |------|
# |------|

# Add newInterval before returning for cases 1) & 3)