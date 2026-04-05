class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l_price = prices[0]
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - l_price)
            l_price = min(l_price, prices[i])

        return max_profit

            