class TrieNode:
    def __init__(self):
        # Using a dict is more memory efficient and flexible
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_end = True

    def search(self, word: str) -> bool:
        return self._dfs(word, 0, self.root)

    def _dfs(self, word: int, index: int, node: TrieNode) -> bool:
        if index == len(word):
            return node.is_end
        
        char = word[index]
        if char == '.':
            # Only iterate over existing children
            for child in node.children.values():
                if self._dfs(word, index + 1, child):
                    return True
            return False
        
        if char in node.children:
            return self._dfs(word, index + 1, node.children[char])
            
        return False

