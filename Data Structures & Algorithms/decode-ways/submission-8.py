class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1] * (len(s) + 1)
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                continue
            dp[i] = dp[i + 1]

            if i < (len(s) - 1) and (s[i] == "1" or (s[i] == "2" and s[i + 1] <= "6")):
                dp[i] += dp[i + 2]

        return dp[0]





# dp[i] = dp[i + 1] + (dp[i + 2] if valid)

# s = "2712"
# dp = [?, ?, ?, ?, 1]