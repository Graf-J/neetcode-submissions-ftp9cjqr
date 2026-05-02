class MedianFinder:
    def __init__(self):
        self.left, self.right = [], []

    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
            if not self.left or self.left[0] > num or self.right[0] > num:
                heapq.heappush_max(self.left, num)
            else:
                right_top = heapq.heapreplace(self.right, num)
                heapq.heappush_max(self.left, right_top)
        else:
            if self.left[0] > num:
                left_top = heapq.heapreplace_max(self.left, num)
                heapq.heappush(self.right, left_top)
            else:
                heapq.heappush(self.right, num)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (self.left[0] + self.right[0]) / 2
        else:
            return self.left[0]
        