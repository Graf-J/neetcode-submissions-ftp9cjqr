class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        chars = [0] * 26
        l = 0

        for r in range(len(s)):
            chars[ord(s[r]) - ord("A")] += 1

            while (r - l + 1) - max(chars) > k:
                chars[ord(s[l]) - ord("A")] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len