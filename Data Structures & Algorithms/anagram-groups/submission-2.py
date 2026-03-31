from collections import defaultdict

class Solution:
    def str2tup(self, string):
        count = [0] * 26
        for char in string:
            idx = ord(char) - ord("a")
            count[idx] += 1
        return tuple(count)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = defaultdict(list)
        for string in strs:
            tup = self.str2tup(string)
            grouped_anagrams[tup].append(string)

        return list(grouped_anagrams.values())