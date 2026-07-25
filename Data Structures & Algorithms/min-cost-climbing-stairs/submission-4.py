class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dfs(i: int) -> int:
            if i == len(cost):
                return 0
            if i > len(cost):
                return float("inf")
            if i in memo:
                return memo[i]

            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return memo[i]

        return min(dfs(0), dfs(1))







    #                 (0)                         (1)
    #                 r:3
    #         (1)             (2)
    #         r:2             r:3
    #     (2)     (3)     (3)     (4)
    #     r:3     r:0     r:0     r:i
    #   (3) (4)
    #   r:0 r:i