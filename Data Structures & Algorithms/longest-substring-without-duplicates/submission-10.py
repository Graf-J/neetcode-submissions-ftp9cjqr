class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        l = 0
        max_seq = 0
        for r in range(len(s)):
            if s[r] in char_map:
                l = max(l, char_map[s[r]] + 1)
            char_map[s[r]] = r
            max_seq = max(max_seq, r - l + 1)

        return max_seq
