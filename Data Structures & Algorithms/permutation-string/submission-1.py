class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_freq = [0] * 26
        for char in s1:
            char_freq[ord(char) - ord("a")] += 1

        q = deque()
        for r in range(len(s2)):
            char_freq[ord(s2[r]) - ord("a")] -= 1
            q.append(s2[r])
            if len(q) > len(s1):
                char = q.popleft()
                char_freq[ord(char) - ord("a")] += 1

            if not any(char_freq):
                return True

        return False





# s1 = "abc"
# s2 = "lecabee"
# char_freq = [0, 0, 0, 0, 0, 0, ..., 0]
# queue = [e, c, a]
# r = 4

