class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have_map, need_map = {}, {}
        for char in t:
            need_map[char] = 1 + need_map.get(char, 0)

        have, need = 0, len(need_map)
        l, best_l, best_r = 0, float("-inf"), float("inf")
        for r in range(len(s)):
            char = s[r]
            if char in need_map:
                have_map[char] = 1 + have_map.get(char, 0)
                if have_map[char] == need_map[char]:
                    have += 1

            while have == need:
                if s[l] in have_map:
                    have_map[s[l]] -= 1
                    if have_map[s[l]] < need_map[s[l]]:
                        have -= 1
                        if best_r - best_l > r - l:
                            best_l, best_r = l, r
                l += 1

        if best_l >= 0:
            return s[best_l:best_r + 1]
        return ""
