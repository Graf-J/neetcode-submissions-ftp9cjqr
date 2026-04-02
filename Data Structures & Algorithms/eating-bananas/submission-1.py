class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_k = float("inf")
        while l <= r:
            k = l + (r - l) // 2
            hours = 0
            for pile in piles:
                hours += -(-pile // k)

            if hours <= h:
                min_k = min(min_k, k)
                r = k - 1
            else:
                l = k + 1

        return min_k