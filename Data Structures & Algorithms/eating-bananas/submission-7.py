class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        current_best = r
        while l <= r:
            eating_rate = (l + r) // 2 # Left Biased
            duration = 0
            for pile in piles:
                duration += -(-pile // eating_rate)

            if duration <= h:
                current_best = eating_rate
                r = eating_rate - 1
            else:
                l = eating_rate + 1

        return current_best
