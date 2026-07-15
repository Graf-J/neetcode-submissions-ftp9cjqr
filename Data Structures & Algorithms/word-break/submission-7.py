class TrieNode:
    __slots__ = "children", "is_end"
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            current = current.children.setdefault(char, TrieNode())
        current.is_end = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        max_word_len = max(len(word) for word in wordDict)

        dp = [False] * (len(s) + 1)
        dp[-1] = True
        for i in range(len(s) - 1, -1, -1):
            current = trie.root
            for c in range(i, min(len(s), i + max_word_len)):
                if s[c] not in current.children:
                    break
                current = current.children[s[c]]
                if current.is_end and dp[c + 1]:
                    dp[i] = True
                    break

        return dp[0]
