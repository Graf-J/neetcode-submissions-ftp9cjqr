class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            i = ord(char) - ord("a")
            if cur.children[i] is None:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.is_end = True

    def search(self, word: str) -> bool:
        def dfs(i, node) -> bool:
            if i == len(word):
                return node.is_end
            if word[i] != "." and node.children[ord(word[i]) - ord("a")] is None:
                return False

            if word[i] == ".":
                return any(dfs(i + 1, child) for child in node.children if child is not None)
            
            return dfs(i + 1, node.children[ord(word[i]) - ord("a")])

        return dfs(0, self.root)
