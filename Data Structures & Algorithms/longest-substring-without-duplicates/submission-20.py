class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_str_len = 0
        char_idx = {}
        l = r = 0
        for r in range(0, len(s)):
            if s[r] in char_idx:
                l = max(char_idx[s[r]] + 1, l)

            char_idx[s[r]] = r
            max_str_len = max(max_str_len, r - l + 1)

        return max_str_len

# s = "pwwkepw"
# hashset = {
#     p: 5
#     w: 6
#     k: 3
#     e: 4

# }
# longest = 4

# l = 2
# r = 6



