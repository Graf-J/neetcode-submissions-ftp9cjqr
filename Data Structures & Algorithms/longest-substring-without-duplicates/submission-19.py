class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        max_str_len = 0
        char_idx = dict()
        l = r = 0
        for r in range(0, len(s)):
            if s[r] in char_idx:
                max_str_len = max(max_str_len, r - l)
                l = max(char_idx[s[r]] + 1, l)

            char_idx[s[r]] = r

        return max(max_str_len, r - l + 1)

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



