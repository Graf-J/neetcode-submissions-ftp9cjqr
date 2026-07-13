class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amount_remaining) -> int:
            if amount_remaining == 0:
                return 0
            if amount_remaining < 0:
                return float("inf")
            if amount_remaining in memo:
                return memo[amount_remaining]

            min_depth = float("inf")
            for c in coins:
                min_depth = min(min_depth, 1 + dfs(amount_remaining - c))

            memo[amount_remaining] = min_depth
            return min_depth

        result = dfs(amount)
        return -1 if result == float("inf") else result