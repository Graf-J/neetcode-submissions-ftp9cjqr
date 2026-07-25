class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 2)
        dp[-1] = float("inf")
        for i in range(len(cost) - 1, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        return min(dp[0], dp[1])



    # dp[i] = nums[i] + min(dp[i + 1], dp[i + 2])

    # dp = [?, ?, ?, 0, inf]
    #      [?, ?, 3, 0, inf]
    #      [?, 2, 3, 0, inf]
    #      [(3), (2), 3, 0, inf]
         



    #                 (0)                         (1)
    #                 r:3
    #         (1)             (2)
    #         r:2             r:3
    #     (2)     (3)     (3)     (4)
    #     r:3     r:0     r:0     r:i
    #   (3) (4)
    #   r:0 r:i