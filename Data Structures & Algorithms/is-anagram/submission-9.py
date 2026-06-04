class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars = [0] * (ord("z") - ord("a") + 1)
        for s_char, t_char in zip(s, t):
            chars[ord(s_char) - ord("a")] += 1
            chars[ord(t_char) - ord("a")] -= 1

        return not any(chars)