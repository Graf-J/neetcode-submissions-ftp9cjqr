class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        # Odd
        dp = [[False] * len(s) for _ in range((len(s) + 1) // 2)]
        for i in range(len(s)):
            dp[0][i] = True
            result += 1
        for i in range(1, (len(s) + 1) // 2):
            for j in range(i, len(s) - i):
                l, r = j - i, j + i
                if dp[i - 1][j] and l >= 0 and r < len(s) and s[l] == s[r]:
                    dp[i][j] = True
                    result += 1
        
        # Even
        dp = [[False] * (len(s) - 1) for _ in range(len(s) // 2)]
        for i in range(len(s) - 1):
            is_palindrome = s[i] == s[i + 1]
            dp[0][i] = is_palindrome
            result += is_palindrome
        for i in range(1, len(s) // 2):
            for j in range(i, len(s) - i - 1):
                l, r = j - i, j + i + 1
                if dp[i - 1][j] and l >= 0 and r < len(s) and s[l] == s[r]:
                    dp[i][j] = True
                    result += 1

        return result





'''

"abaab"

"a", "b", "a", "a", "b"
"aa"
"aba"
"baab"

"ab", "ba", "aa", "ab"

5 -> 3 -> 1 -> x (3 iterations)
6 -> 4 -> 2 -> x (3 iterations) (len + 1) // 2

[T, T, T, T, T]
[x, T, ., ., x]
[x, x, ., x, x]
[x, x, x, x, x]

5: 4 -> 2 -> x
6: 5 -> 3 -> 1 -> x len // 2

[., ., T, .]
[x, ., T, x]
[x, x, x, x]

'''