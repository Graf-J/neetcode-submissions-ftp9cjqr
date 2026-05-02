class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        while len(nums) > self.k:
            heapq.heappop(nums)
        self.nums = nums

    def add(self, val: int) -> int:
        if len(self.nums) == self.k:
            heapq.heappushpop(self.nums, val)
        else:
            heapq.heappush(self.nums, val)

        return self.nums[0]
