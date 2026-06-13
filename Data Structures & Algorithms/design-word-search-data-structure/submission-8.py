class TrieNode:
    __slots__ = ("children", "is_end")
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            current = current.children.setdefault(char, TrieNode())
        current.is_end = True

    def search(self, word: str) -> bool:
        def dfs(current, i):
            if i == len(word):
                return current.is_end

            if word[i] == ".":
                # for node in current.children.values():
                #     exists = dfs(node, i + 1)
                #     if exists:
                #         return True
                # return False
                return any(dfs(node, i + 1) for node in current.children.values())
            else:
                if word[i] in current.children:
                    return dfs(current.children[word[i]], i + 1)
                return False

        return dfs(self.root, 0)






