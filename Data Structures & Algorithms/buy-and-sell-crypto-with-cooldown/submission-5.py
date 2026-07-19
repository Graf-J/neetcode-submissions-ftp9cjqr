class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ht_i1 = prices[-1]
        hf_i1 = hf_i2 = 0
        for i in range(n - 2, -1, -1):
            ht_new = max(ht_i1, prices[i] + hf_i2)
            hf_new = max(hf_i1, -prices[i] + ht_i1)
            ht_i1, hf_i1, hf_i2 = ht_new, hf_new, hf_i1

        return hf_i1
        

        # n = len(prices)
        # dp = [[0] * (n + 1) for _ in range(2)]
        # dp[True][-2] = prices[-1]
        # for i in range(n - 2, -1, -1):
        #     dp[True][i] = max(dp[True][i + 1], prices[i] + dp[False][i + 2])
        #     dp[False][i] = max(dp[False][i + 1], -prices[i] + dp[True][i + 1])

        # return dp[False][0]