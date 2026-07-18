class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}
        def dfs(i: int, b: int):
            if i >= n:
                return 0
            if (i, b) in memo:
                return memo[(i, b)]

            if b >= 0: # Can choose to sell
                memo[(i, b)] = max((prices[i] - prices[b]) + dfs(i + 2, -1), dfs(i + 1, b))
            else: # Can choose to buy
                memo[(i, b)] = max(dfs(i + 1, i), dfs(i + 1, -1))

            return memo[(i, b)]

        return dfs(0, -1)







        #                 O
        #     buy(0)                skip(0)
        # sell(1)    skip(1)   buy(1)      skip(1)
