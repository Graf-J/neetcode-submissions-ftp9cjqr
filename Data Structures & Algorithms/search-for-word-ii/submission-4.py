class TrieNode:
    __slots__ = ("children", "is_end", "word")

    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = ""

class Solution:
    def __init__(self) -> None:
        self.root = TrieNode()

    def trie_insert(self, word: str) -> None:
        current = self.root
        for char in word:
            current = current.children.setdefault(char, TrieNode())
        current.is_end = True
        current.word = word

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Metadata
        width, height = len(board[0]), len(board)

        # Build Trie first
        for word in words:
            self.trie_insert(word)

        # DFS: Check if Word exists
        result = set()
        visited = set()
        def dfs(node: TrieNode, row: int, col: int) -> None:
            if node.is_end:
                result.add(node.word)

            directions = ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1))
            for r, c in directions:
                if (r < 0 or c < 0 or
                    r == height or c == width or
                    (r, c) in visited or
                    board[r][c] not in node.children
                ):
                    continue

                visited.add((r, c))
                dfs(node.children[board[r][c]], r, c)
                visited.remove((r, c))

        # Go through all Starting-Points
        for row in range(height):
            for col in range(width):
                if board[row][col] in self.root.children:
                    visited.add((row, col))
                    dfs(self.root.children[board[row][col]], row, col)
                    visited.remove((row, col))

        return list(result)







