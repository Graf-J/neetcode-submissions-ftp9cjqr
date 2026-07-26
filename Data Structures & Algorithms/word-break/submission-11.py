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
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        for i in range(len(s) - 1, -1, -1):
            current = trie.root
            for j in range(i, len(s)):
                if s[j] not in current.children:
                    break
                current = current.children[s[j]]
                if current.is_end:
                    dp[i] |= dp[j + 1]

        return dp[0]


# s = "neetcode", wordDict = ["neet", "code"]

# dp[i] = dp[i + len(w) if w in s at j]
# dp = [?, ?, ?, ?, ?, ?, ?, T]



            #             (0)
            # (3)                     (4)
            # (6)                     (6)
            # (9)