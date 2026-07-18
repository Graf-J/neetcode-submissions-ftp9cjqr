class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp_current = [0] * (len(text2) + 1)
        dp_last = [0] * (len(text2) + 1)

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp_current[j] = 1 + dp_last[j + 1]
                else:
                    dp_current[j] = max(dp_current[j], dp_current[j + 1])

            dp_last = dp_current.copy()

        return dp_current[0]

        # dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        # for i in range(len(text1) - 1, -1, -1):
        #     for j in range(len(text2) - 1, -1, -1):
        #         if text1[i] == text2[j]:
        #             dp[i][j] = 1 + dp[i + 1][j + 1]
        #         else:
        #             dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        # return dp[0][0]








# df[i][j] = 1 + dfs[i + 1][j + 1] or max(dfs[i + 1][j], dfs[i][j + 1])

# text1 = "crabt"
# text2 = "cat"
#         0:c 1:a 2:t dummy
# 0:c                   0
# 1:r                   0
# 2:a                   0
# 3:b                   0
# 4:t             1     0 
# dummy   0   0   0     0
