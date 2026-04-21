class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_map = defaultdict(int)
        for char in t:
            char_map[char] += 1

        l, best_l, best_r = 0, float("-inf"), float("inf")
        for r in range(len(s)):
            char = s[r]
            if char in char_map:
                char_map[char] -= 1
            
            if all(count <= 0 for count in char_map.values()):
                while all(count <= 0 for count in char_map.values()):
                    if s[l] in char_map:
                        char_map[s[l]] += 1
                    l += 1

                if (r - l + 1) < (best_r - best_l):
                    best_l, best_r = l - 1, r

        if best_l >= 0:
            return s[best_l:best_r + 1]
        return ""

                