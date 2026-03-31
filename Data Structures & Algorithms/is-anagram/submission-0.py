from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap_s, hashmap_t = defaultdict(int), defaultdict(int)
        for char_s, char_t in zip(s, t):
            hashmap_s[char_s] += 1
            hashmap_t[char_t] += 1

        for key_s, value_s in hashmap_s.items():
            if hashmap_t[key_s] != value_s:
                return False

        return True

        
