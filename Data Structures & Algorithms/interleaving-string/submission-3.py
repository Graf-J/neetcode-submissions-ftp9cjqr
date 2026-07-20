class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[-1][-1] = True
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i == len(s1) and j == len(s2):
                    continue

                dp[i][j] = (
                    (i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]) or
                    (j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1])
                )

        return dp[0][0]



# dp[i][j] = (i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]) or (j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1])

# s1 = aaa
# s2 = bbb
# s3 = aabbba

# Initial State
#     0:b 1:b 2:b 3:d
# 0:a              
# 1:a              
# 2:a             
# 3:d              T


#     0:b 1:b 2:b 3:d
# 0:a              
# 1:a              
# 2:a          T   T
# 3:d  F   F   F   T



#                                 O: (0,0)
#                 a: (1,0)                             x
#         a: (2,0)
#                 b: (2,1)
#                         b: (2,2)
#                                 b: (2,3)
#                         a: (3,3)


