class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            first, second = heapq.heappop_max(stones), heapq.heappop_max(stones)
            if first < second:
                heapq.heappush_max(stones, second - first)
            elif second < first:
                heapq.heappush_max(stones, first - second)

        return stones[0] if len(stones) == 1 else 0

        