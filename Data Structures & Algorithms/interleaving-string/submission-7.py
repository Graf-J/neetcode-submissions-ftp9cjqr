class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}
        def dfs(i: int, j: int) -> bool:
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in memo:
                return memo[(i, j)]
            
            if (
                i < len(s1) and s1[i] == s3[i + j] and
                j < len(s2) and s2[j] == s3[i + j]
            ):
                memo[(i, j)] = dfs(i + 1, j) or dfs(i, j + 1)
                return memo[(i, j)]
            
            if i < len(s1) and s1[i] == s3[i + j]:
                memo[(i, j)] = dfs(i + 1, j)
                return memo[(i, j)]

            if j < len(s2) and s2[j] == s3[i + j]:
                memo[(i, j)] = dfs(i, j + 1)
                return memo[(i, j)]

            memo[(i, j)] = False
            return False

        return dfs(0, 0)








        #                 (0,0)
        # (1,0)                           (0,1)