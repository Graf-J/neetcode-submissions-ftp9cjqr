class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i: int, remaining: int) -> int:
            if remaining == 0:
                return 1
            if i == len(coins) or remaining < 0:
                return 0
            if (i, remaining) in memo:
                return memo[(i, remaining)]

            memo[(i, remaining)] = dfs(i, remaining - coins[i]) + dfs(i + 1, remaining)
            return memo[(i, remaining)]

        return dfs(0, amount)
        
        
        
        
        
        
#                         []
#             [1]                         []
#     [1,1]           [1]         [2]             []
# [1,1,1] [1,1]   [1,2]  [1] [2,2]  [2]       [3]     []

        