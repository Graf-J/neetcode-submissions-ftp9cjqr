class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amt_left: int) -> int:
            if amt_left == 0:
                return 0
            if amt_left < 0:
                return float("inf")
            
            min_coins = float("inf")
            for c in coins:
                if amt_left - c in memo:
                    min_coins = min(min_coins, memo[amt_left - c])
                else:
                    min_coins = min(min_coins, dfs(amt_left - c))

            memo[amt_left] = min_coins + 1
            return memo[amt_left]

        result = dfs(amount)
        return -1 if result == float("inf") else result
        








#                     12
#         11          7           2
#     10      6   6       2       1
# 9   5   0 5    1   5    1       0
        








# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# [1, ?, ?, ?, 1, ?, ?, ?, ?, 1,  ?,  ?]
# [1, 2, ?, ?, 1, 2, ?, ?, ?, 1,  2,  ?]

# dp[i] = 
    