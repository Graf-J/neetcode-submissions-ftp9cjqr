class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[0] * len(board[0]) for _ in board]
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or word[i] != board[r][c] or visited[r][c]:
                return False

            visited[r][c] = 1
            result = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )
            visited[r][c] = 0
            return result

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        return False