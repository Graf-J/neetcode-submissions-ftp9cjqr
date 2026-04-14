class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        result = float("inf")
        l, r = 1, max(piles)
        while l <= r:
            k = (l + r) // 2
            takes_hours = 0
            for pile in piles:
                takes_hours += -(-pile // k)

            if takes_hours <= h:
                result = min(result, k)
                r = k - 1
            else:
                l = k + 1
        return result