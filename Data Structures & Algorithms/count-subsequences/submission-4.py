class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        dp[len(s)][len(t)] = 1
        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t), -1, -1):
                dp[i][j] = dp[i + 1][j]
                if j < len(t) and s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]

        return dp[0][0]


# dp[i][j] = dp[i + 1][j] + (dp[i + 1][j + 1] if j < len(t) and s[i] == t[j])

#     j:0 j:1 j:2 j:3
# i:0
# i:1
# i:2
# i:3
# i:4              
# i:5  0   0   0   1



            #             (0,0)
            # (1,0)                   (1,1)
            #                 (2,1)           (2,2)
            #             (3,1)   (3,2)