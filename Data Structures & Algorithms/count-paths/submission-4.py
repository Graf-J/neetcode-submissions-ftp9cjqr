class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Base Case
        dp = [[-1] * (n + 1) for _ in range(m + 1)]
        for r in range(m + 1):
            dp[r][-1] = 0
        for c in range(n):
            dp[-1][c] = 0
        dp[m - 1][n - 1] = 1

        # Reoccurence
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if dp[r][c] == -1:
                    dp[r][c] = dp[r + 1][c] + dp[r][c + 1]

        return dp[0][0]




# dp[r][c] = dp[r + 1][c] + dp[r][c + 1]
# => New Cell is sum of right and bottom cell

# Base-Case (Dummy row and col)
# [ ][ ][ ][0]
# [ ][ ][1][0]
# [0][0][0][0]

# [3][2][1][0]
# [1][1][0][0]
# [0][0][0][0]

# => Strategy: Start with last row from right to left since it always has the right and bottom neighbor