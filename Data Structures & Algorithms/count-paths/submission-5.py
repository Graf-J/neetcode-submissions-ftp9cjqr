class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(m - 1):
            for i in range(n - 2, -1, -1):
                dp[i] += dp[i + 1]

        return dp[0]





# dp[r][c] = dp[r + 1][c] + dp[r][c + 1]
# => New Cell is sum of right and bottom cell

# Space Optimization:
# We need only one row since we only need the last row to generate the next row

# Example (m=3, n=4)
# [ ][ ][ ][ ]
# [ ][ ][ ][ ]
# [ ][ ][ ][ ]

# Full Result
# [10][6][3][1]
# [4][3][2][1]
# [1][1][1][1]


# 1) dp = [1, 1, 1, 1]

# 2) dp = [?, ?, ?, 1]
#    dp = [+=3 = 4, +=2 = 3, +=1 = 2, 1]
#    dp = [4, 3, 2, 1]

# 3) dp = [?, ?, ?, 1]
#    dp = [+= 6 = 10, +=3 = 6, +=1 = 3, 1]


# => Calculate from right to left and alwas update inplace
# => The old value basically is the bottom value for the next iteration