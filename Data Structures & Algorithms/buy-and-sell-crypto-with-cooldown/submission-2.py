class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * (n + 1) for _ in range(2)]
        dp[True][-2] = prices[-1]
        for i in range(n - 2, -1, -1):
            dp[True][i] = max(dp[True][i + 1], prices[i] + dp[False][i + 2])
            dp[False][i] = max(dp[False][i + 1], -prices[i] + dp[True][i + 1])

        return dp[False][0]



# holding: True  dp[holding][i] = max(dp[holding][i + 1], prices[i] + dp[not holding][i + 2])
# holding: False dp[holding][i] = max(dp[holding][i + 1], -prices[i] + dp[not holding][i + 1])



#                 1   3   4   0   4   dummy
# holding: True                   4   0
# holding: False                  0   0











