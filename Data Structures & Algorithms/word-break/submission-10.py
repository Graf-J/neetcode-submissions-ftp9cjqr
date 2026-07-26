class TrieNode:
    __slots__ = "children", "is_end"

    def __init__(self) -> None:
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            current = current.children.setdefault(c, TrieNode())
        current.is_end = True


class Solution:
    def build_trie(self, words: List[str]) -> Trie:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = self.build_trie(wordDict)
        dead_ends = set() # Memoization
        def dfs(i: int) -> bool:
            if i == len(s):
                return True
            if i in dead_ends:
                return False

            current = trie.root
            for j in range(i, len(s)):
                if s[j] not in current.children:
                    break
                current = current.children[s[j]]
                if current.is_end:
                    if dfs(j + 1):
                        return True

            dead_ends.add(i)
            return False

        return dfs(0)









            #             (0)
            # (3)                     (4)
            # (6)                     (6)
            # (9)