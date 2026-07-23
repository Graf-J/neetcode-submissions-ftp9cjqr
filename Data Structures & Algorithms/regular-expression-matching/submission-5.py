class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [False] * (len(p) + 1)
        dp[len(p)] = True
        for i in range(len(s), -1, -1):
            dp_next = [False] * (len(p) + 1)
            dp_next[len(p)] = (i == len(s))
            for j in range(len(p) - 1, -1, -1):
                chars_match = i < len(s) and (s[i] == p[j] or p[j] == ".")
                if j < len(p) - 1 and p[j + 1] == "*":
                    dp_next[j] = dp_next[j + 2] or (chars_match and dp[j])
                elif chars_match:
                    dp_next[j] = dp[j + 1]
                else:
                    dp_next[j] = False
            dp = dp_next

        return dp[0]




