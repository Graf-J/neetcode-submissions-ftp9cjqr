class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dfs(i: int, j: int) -> int:
            if j == len(word2):
                return len(word1) - i
            if i == len(word1):
                return len(word2) - j
            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]

            memo[(i, j)] = 1 + min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))
            return memo[(i, j)]

        return dfs(0, 0)


#         012345678
# word1 = dmonkeis
#         012345
# word2 = money


#                                     (0,0)
#                 (1,0)               (0,1)               (1,1)
#                 (2,1)
#                 (3,2)
#                 (4,3)
#         (5,3)   (4,4)   (5,4)
#         (6,4)
# (7,4)   (6,5)   (7,5)

