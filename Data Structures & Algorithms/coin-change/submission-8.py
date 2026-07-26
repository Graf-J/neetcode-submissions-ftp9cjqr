class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for r in range(1, amount + 1):
            result = float("inf")
            for c in coins:
                if r - c >= 0:
                    result = min(result, 1 + dp[r - c])
            dp[r] = result

        return -1 if dp[amount] == float("inf") else dp[amount]







# dp[r] = min(dp[r - c] for c in coins)

# dp = [0,]




        #                 (12)
        #                 r:3
        # (11)            (7)             (2)
        #                                 r:2
        #                         (1)     (-3)       (-8)
        #                         r:1     r:i         r:i
        #                     (0) (-4) (-9)
        #                     r:0  r:i i:i

