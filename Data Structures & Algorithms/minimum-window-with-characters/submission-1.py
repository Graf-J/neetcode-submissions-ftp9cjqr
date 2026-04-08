from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Initialize Char Map
        char_map = defaultdict(int)
        for char in t:
            char_map[char] += 1

        min_l, min_r = float("-inf"), float("inf")
        l = 0
        for r in range(len(s)):
            if s[r] in char_map:
                char_map[s[r]] -= 1

            if all(x <= 0 for x in char_map.values()):
                while l <= r and all(x <= 0 for x in char_map.values()):
                    if s[l] in char_map:
                        char_map[s[l]] += 1
                    if (r - l + 1) < (min_r - min_l + 1):
                        min_l, min_r = l, r
                    l += 1

        if min_l >= 0 and min_r < len(s):
            return s[min_l : min_r + 1]
        return ""

            