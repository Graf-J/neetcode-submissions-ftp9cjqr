class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dfs(i: int, j: int) -> int:
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + dfs(i + 1, j + 1)
                return memo[(i, j)]
            else:
                memo[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
                return memo[(i, j)]

        return dfs(0, 0)








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
                            