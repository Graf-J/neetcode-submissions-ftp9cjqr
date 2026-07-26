class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(r: int) -> int:
            if r == 0:
                return 0
            if r < 0:
                return float("inf")
            if r in memo:
                return memo[r]

            result = float("inf")
            for c in coins:
                result = min(result, 1 + dfs(r - c))

            memo[r] = result
            return result

        result = dfs(amount)
        return -1 if result == float("inf") else result











        #                 (12)
        #                 r:3
        # (11)            (7)             (2)
        #                                 r:2
        #                         (1)     (-3)       (-8)
        #                         r:1     r:i         r:i
        #                     (0) (-4) (-9)
        #                     r:0  r:i i:i

