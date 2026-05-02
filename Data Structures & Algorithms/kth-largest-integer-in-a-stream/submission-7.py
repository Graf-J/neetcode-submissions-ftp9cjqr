class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = []
        for num in nums:
            self._add_to_stream(num)

    def _add_to_stream(self, num):
        if len(self.stream) == self.k:
            heapq.heappushpop(self.stream, num)
        else:
            heapq.heappush(self.stream, num)

    def add(self, val: int) -> int:
        self._add_to_stream(val)
        return self.stream[0]
        
