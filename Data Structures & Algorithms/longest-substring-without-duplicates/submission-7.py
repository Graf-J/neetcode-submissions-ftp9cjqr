class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        store = {}
        l, r = 0, 0
        while r < len(s):
            if s[r] in store:
                longest_substring = max(longest_substring, r - l)
                l = max(l, store[s[r]] + 1)

            store[s[r]] = r
            r += 1

        return max(longest_substring, r - l)

        
