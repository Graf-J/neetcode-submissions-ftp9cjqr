class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_ctr = [0] * 26
        for c_s, c_t in zip(s, t):
            char_ctr[ord(c_s) - ord("a")] += 1
            char_ctr[ord(c_t) - ord("a")] -= 1

        return not any(char_ctr)
