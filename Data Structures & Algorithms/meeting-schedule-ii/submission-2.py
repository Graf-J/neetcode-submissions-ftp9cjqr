"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0 

        intervals.sort(key=lambda x: x.start)

        heap = [intervals[0].end]
        for i in range(1, len(intervals)):
            if heap[0] <= intervals[i].start:
                heapq.heapreplace(heap, intervals[i].end)
            else:
                heapq.heappush(heap, intervals[i].end)

        return len(heap)    


