class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[1] * (amount + 1) for _ in range(len(coins))]
        dp.append([0] * (amount + 1))
        for remaining in range(1, amount + 1):
            for c_idx in range(len(coins) - 1, -1, -1):
                tmp = 0 if remaining - coins[c_idx] < 0 else dp[c_idx][remaining - coins[c_idx]]
                dp[c_idx][remaining] = tmp + dp[c_idx + 1][remaining]

        return dp[0][-1]



# dp[i][remaining] = dp[i][remaining - c] + dp[i + 1][remaining]

#     0   1   2   3   4   (remaining)   
# 1   1   1   2   3   4
# 2   1   0   1   1   1
# 3   1   0   0   1   0
# d   0   0   0   0   0

# (i)