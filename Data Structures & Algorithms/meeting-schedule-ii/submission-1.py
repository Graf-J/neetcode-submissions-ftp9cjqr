"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted(interval.start for interval in intervals)
        end = sorted(interval.end for interval in intervals)

        result = 0
        count = 0
        s = e = 0
        while s < len(start):
            if end[e] <= start[s]:
                count -= 1
                e += 1
            else:
                count += 1
                s += 1
                result = max(result, count)

        return result
        