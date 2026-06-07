class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        char_count = defaultdict(int)
        max_freq = 0
        max_win_len = 0
        for r in range(len(s)):
            char_count[s[r]] += 1
            max_freq = max(max_freq, char_count[s[r]])
            while (r - l + 1) - max_freq > k:
                char_count[s[l]] -= 1
                l += 1

            max_win_len = max(max_win_len, r - l + 1)

        return max_win_len



# "ABAAAAC"


# k = 3
# s = "ABCBABCBBB"

# max_win = 
# max_freq = 2
# l = 0
# r = 4

# (r - l + 1) = 5
# 5 - max_frq = 3

# {
#     A: 2
#     B: 2
#     C: 1
# }
