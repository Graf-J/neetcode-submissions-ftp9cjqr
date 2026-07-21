class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for j in range(len(word2) - 1, -1, -1):
            dp[-1][j] = len(word2) - j
        for i in range(len(word1) - 1, -1, -1):
            dp[i][-1] = len(word1) - i

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])

        return dp[0][0]


# word1 = dmonkeis
# word2 = money

#     0:m 1:o 2:n 3:e 4:y 5:/     word2(j)
# 0:d                      8                     
# 1:m                      7
# 2:o                      6
# 3:n                      5
# 4:k                      4
# 5:e                      3
# 6:i                      2
# 7:s                      1
# 8:/  5   4   3   2   1   0

# word1(i)


