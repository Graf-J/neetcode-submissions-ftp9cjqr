class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindrome = ""
        for i in range(len(s)):
            l, r = i - 1, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
            if (r - 1) - (l + 1) + 1 > len(max_palindrome):
                max_palindrome = s[(l + 1):r]

        for i in range(len(s) - 1):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
            if (r - 1) - (l + 1) + 1 > len(max_palindrome):
                max_palindrome = s[(l + 1):r]

        return max_palindrome
