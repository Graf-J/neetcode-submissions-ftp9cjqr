class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0] * (len(t) + 1)
        dp[-1] = 1

        for i in range(len(s) - 1, -1, -1):
            dp_next = [1] * (len(t) + 1)
            for j in range(len(t) - 1, -1, -1):
                dp_next[j] = dp[j] + (dp[j + 1] if s[i] == t[j] else 0)
            dp = dp_next

        return dp[0]