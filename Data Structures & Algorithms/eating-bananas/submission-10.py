class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            k = (l + r) // 2
            h_until_finished = 0
            for pile in piles:
                h_until_finished += math.ceil(pile / k)

            if h_until_finished <= h:
                r = k
            else:
                l = k + 1

        return l





# [1, 2, 3, 4]
#  l 
#     r
#  k



# [1, 4, 3, 2]

# k = 1: 10 -> False
# k = 2: 6  -> True
# k = 3: 5  -> True
# k = 4: 4  -> True

# r = m