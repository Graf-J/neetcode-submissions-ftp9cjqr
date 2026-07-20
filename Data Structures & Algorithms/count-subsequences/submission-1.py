class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[1] * (len(t) + 1) for _ in range(len(s))]
        dp.append([0] * (len(t) + 1))
        dp[-1][-1] = 1

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                dp[i][j] = dp[i + 1][j] + (dp[i + 1][j + 1] if s[i] == t[j] else 0)

        return dp[0][0]



# dp[i][j] = dp[i + 1][j] + dp[i + 1][j + 1] if s[i] == t[j] else 0

# s = xxyxy
# t = xy

#     0:x 1:y 2:d     (t/j)
# 0:x          1
# 1:x          1
# 2:y          1
# 3:x          1
# 4:y          1
# 5:d  0   0   1

# (s/i)


#     0:x 1:y 2:d     (t/j)
# 0:x  5   2   1
# 1:x  3   2   1
# 2:y  1   2   1
# 3:x  1   1   1
# 4:y  0   1   1
# 5:d  0   0   1

# (s/i)



