class Solution:
    def countSubstrings(self, s: str) -> int:
        result = len(s)

        for c in range(len(s)):
            l, r = c - 1, c + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
                result += 1

        for c in range(len(s) - 1):
            l, r = c, c + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
                result += 1

        return result