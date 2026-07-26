class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * (len(prices) + 2) for _ in range(2)]
        for i in range(len(prices) - 1, -1, -1):
            # Holding
            dp[0][i] = max(
                dp[0][i + 1], 
                prices[i] + dp[1][i + 2]
            )
            # Not Holding
            dp[1][i] = max(
                dp[1][i + 1],
                -prices[i] + dp[0][i + 1]
            )

        return dp[1][0]




#                 0   1   2   3   4   d   d
# Holding                             0   0
# Not Holding                         0   0




    #                             (0,-)
    #             (1,-)                           (1,h)
    #     (2,-)           (2,h)           (2,-)           (2,h)
    # (3,-)   (3,h)   (3,-)    (3,h)  (3,-)   (3,h)   (3,-)   (3,h)
     