class Solution:
    def string_to_tuple(self, s: str) -> tuple:
        result = [0] * (ord("z") - ord("a") + 1)
        for char in s:
            result[ord(char) - ord("a")] += 1
        return tuple(result)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            t = self.string_to_tuple(s)
            anagrams[t].append(s)

        return list(anagrams.values())