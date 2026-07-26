class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i: int, holding: bool) -> int:
            if i >= len(prices):
                return 0
            if (i, holding) in memo:
                return memo[(i, holding)]
            
            if holding:
                memo[(i, holding)] = max(
                    dfs(i + 1, True), # Still don't sell
                    prices[i] + dfs(i + 2, False) # Sell
                )
            else:
                memo[(i, holding)] = max(
                    dfs(i + 1, False), # Still don't buy
                    -prices[i] + dfs(i + 1, True) # Buy
                )
                
            return memo[(i, holding)]

        return dfs(0, False)










    #                             (0,-)
    #             (1,-)                           (1,h)
    #     (2,-)           (2,h)           (2,-)           (2,h)
    # (3,-)   (3,h)   (3,-)    (3,h)  (3,-)   (3,h)   (3,-)   (3,h)
     