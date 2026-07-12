class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = cost[-2:]
        for i in range(len(cost) - 3, -1, -1):
            one, two = cost[i] + min(one, two), one
        return min(one, two)







# [1, 2, 1, 2, 1, 1, 2]
# [?, ?, ?, ?, ?, 1, 2] (Base Case)
#              ^
# 1 + min(1, 2) = 2

# [1, 2, 1, 2, 1, 1, 2]
# [?, ?, ?, ?, 2, 1, 2] (Base Case)
#           ^

# 2 + min(2, 1) = 3