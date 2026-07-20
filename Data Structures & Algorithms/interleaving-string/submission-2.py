class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}
        def dfs(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(s1) and j == len(s2):
                return True
            if i < len(s1) and s1[i] == s3[i + j]:
                if dfs(i + 1, j):
                    return True
            if j < len(s2) and s2[j] == s3[i + j]:
                if dfs(i, j + 1):
                    return True

            memo[(i, j)] = False
            return False

        return dfs(0, 0)


# s1 = aaa
# s2 = bbb
# s3 = aabbba

#                                 O: (0,0)
#                 a: (1,0)                             x
#         a: (2,0)
#                 b: (2,1)
#                         b: (2,2)
#                                 b: (2,3)
#                         a: (3,3)


