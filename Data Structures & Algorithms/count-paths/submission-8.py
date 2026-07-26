class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp_prev = [0] * (n + 1)
        for r in range(m - 1, -1, -1):
            dp_cur = [0] * (n + 1)
            if r == m - 1:
                dp_cur[n - 1] = 1
            for c in range(n - 1, -1, -1):
                dp_cur[c] = dp_cur[c] + dp_prev[c] + dp_cur[c + 1]
            dp_prev = dp_cur
            
        return dp_prev[0]


# dp[r][c] = dp[r + 1][c] + dp[r][c + 1]

# [?, ?, ?, 0]
# [?, ?, 1, 0]
# [0, 0, 0, 0]




        #                 (0,0)
        #                 r:2
        #     (1,0)                   (0,1)
        #     r:1                     r:1
        # (2,0)   (1,1)           (1,1)   (0,2)
        # r:0     r:1             r:1     r:0