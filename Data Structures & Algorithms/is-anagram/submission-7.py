class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_freq = [0] * (ord("z") - ord("a") + 1)
        for char_s, char_t in zip(s, t):
            char_freq[ord(char_s) - ord("a")] += 1
            char_freq[ord(char_t) - ord("a")] -= 1

        return not any(char_freq)