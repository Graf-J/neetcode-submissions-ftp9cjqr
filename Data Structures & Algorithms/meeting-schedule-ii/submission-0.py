"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda x: x.start)

        rooms = 1
        heap = [intervals[0].end]
        for i in range(1, len(intervals)):
            if intervals[i].start < heap[0]: # No free room
                rooms += 1
                heapq.heappush(heap, intervals[i].end)
            else: # Add to smallest room
                heapq.heapreplace(heap, intervals[i].end)

        return rooms





# [(0, 10), (5, 7), (10, 11)]

# Room 1)   (0,          10)(10,11)
# Room 2)         (5,  7)






