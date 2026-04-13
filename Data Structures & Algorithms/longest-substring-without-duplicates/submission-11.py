class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, max_sequence, cache = 0, 0, {}
        for r in range(len(s)):
            if s[r] in cache:
                l = max(l, cache[s[r]] + 1)
            cache[s[r]] = r
            max_sequence = max(max_sequence, r - l + 1)

        return max_sequence
