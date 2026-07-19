class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i: int, holding: bool) -> int:
            if i >= len(prices):
                return 0
            if (i, holding) in memo:
                return memo[(i, holding)]

            skip = dfs(i + 1, holding)
            if holding:
                sell = prices[i] + dfs(i + 2, False)
                memo[(i, holding)] = max(skip, sell)
            else:
                buy = -prices[i] + dfs(i + 1, True)
                memo[(i, holding)] = max(skip, buy)
                
            return memo[(i, holding)]

        return dfs(0, False)





