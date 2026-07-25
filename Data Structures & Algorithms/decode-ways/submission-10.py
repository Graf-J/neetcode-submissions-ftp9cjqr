class Solution:
    def numDecodings(self, s: str) -> int:
        next1 = 1  # dp[i+1]
        next2 = 0  # dp[i+2]

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                current = 0
            else:
                current = next1
                if (
                    i + 1 < len(s)
                    and (s[i] == "1" or (s[i] == "2" and s[i + 1] <= "6"))
                ):
                    current += next2

            next1, next2 = current, next1

        return next1