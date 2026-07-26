class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]
 


# if text1[i] == text2[j]:
#     dp[i][j] = 1 + dp[i + 1][j + 1]
# else:
#     dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])



# text1 = "cat", text2 = "crabt" 

#                             (0,0)
#                             r:3
#                             (1,1)
#                             r:2
#                 (2,1)                   (1,2)
#                 r:1                     r:2
#         (3,1)           (2,2)           (2,3)
#         r:0             r:1             r:1
#                                     (3,3)   (2,4)
#                                      r.0     r:1
#                                             (3,5)
#                                             r:0
                            