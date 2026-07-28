class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            for r in range(1, amount + 1):
                if r - coins[i] >= 0:
                    dp[r] += dp[r - coins[i]]

        return dp[amount]





# dp[i][remaining] = dp[i][remaining - coins[i]] + dp[i + 1][remaining]

#     r:0 r:1 r:2 r:3 r:4
# i:0  1
# i:1  1
# i:2  1
# i:d  1