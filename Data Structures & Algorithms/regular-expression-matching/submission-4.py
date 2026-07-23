class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[len(s)][len(p)] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                chars_match = i < len(s) and (s[i] == p[j] or p[j] == ".")
                if j < len(p) - 1 and p[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2] or (chars_match and dp[i + 1][j])
                elif chars_match:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = False

        return dp[0][0]




