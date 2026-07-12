class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        result = 1
        # Initialize State
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1):
            dp[i][i] = True
            dp[i][i + 1] = s[i] == s[i + 1]
            result += 1 + (s[i] == s[i + 1])
        dp[n - 1][n - 1] = True

        # Run DP-Algorithm (start at length = 3)
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                l, r = i, i + length - 1
                if dp[l + 1][r - 1] and s[l] == s[r]:
                    dp[l][r] = True
                    result += 1

        return result


'''

"abaab"

# Initialize State
  a  b  a  a  b
a 1  0  ?  ?  ?
b x  1  0  ?  ?
a x  x  1  1  ?
a x  x  x  1  0
b x  x  x  x  1


'''


