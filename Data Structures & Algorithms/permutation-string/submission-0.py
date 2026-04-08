class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Protect l, r = 0, len(s1)
        if len(s2) < len(s1):
            return False

        # Build Map
        s1_map = [0] * 26
        for char in s1:
            s1_map[ord(char) - ord("a")] += 1

        # Calculate for Initial Window
        l, r = 0, len(s1) - 1
        for i in range(len(s1)):
            s1_map[ord(s2[i]) - ord("a")] -= 1

        # Move Static Window over String
        while r < len(s2):
            if all(c == 0 for c in s1_map):
                return True

            s1_map[ord(s2[l]) - ord("a")] += 1
            l, r = l + 1, r + 1
            if r < len(s2):
                s1_map[ord(s2[r]) - ord("a")] -= 1

        return False