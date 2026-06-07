class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, cache, max_len = 0, {}, 0
        for r in range(len(s)):
            if s[r] in cache:
                l = max(l, cache[s[r]] + 1)

            max_len = max(max_len, r - l + 1)
            cache[s[r]] = r

        return max_len



