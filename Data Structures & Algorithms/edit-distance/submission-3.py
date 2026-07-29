class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for r in range(len(word1) + 1):
            dp[r][len(word2)] = len(word1) - r
        for c in range(len(word2) + 1):
            dp[len(word1)][c] = len(word2) - c

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i + 1][j],      # delete
                        dp[i][j + 1],      # insert
                        dp[i + 1][j + 1]   # replace
                    )

        return dp[0][0]
 

# dp[i][j] = (
#     if word1[i] == word2[j]:
#         dp[i + 1][j + 1]
#     else:
#         1 + min(
#             dp[i + 1][j],      # delete
#             dp[i][j + 1],      # insert
#             dp[i + 1][j + 1]   # replace
#         )
# )
#     j:0 j:1 j:2 j:3
# i:0              4
# i:1              3
# i:2              2
# i:3              1
# i:4  3   2   1   0


        #             (0,0)
        # (1,0)       (0,1)       (1,1)
        # delete      insert      replace