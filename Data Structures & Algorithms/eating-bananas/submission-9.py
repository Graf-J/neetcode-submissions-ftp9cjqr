class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            k = (l + r) // 2 # Left-Biased
            duration = 0
            for pile in piles:
                duration += math.ceil(pile / k)
            
            if duration > h: # Invalid -> Have to chooose bigger eating-rate k
                l = k + 1
            else:
                r = k

        return l









# Left-Biased

# [1, 2, 3, 4]
#     l  r









