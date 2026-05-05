class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        width, height = len(board[0]), len(board)

        def dfs(row, col, k, visited):
            if board[row][col] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            if board[row][col] != word[k]:
                return False

            visited[row][col] = True

            is_left = is_right = is_top = is_bottom = False

            if col > 0 and not visited[row][col-1]:
                is_left = dfs(row, col-1, k+1, visited)

            if col < width - 1 and not visited[row][col+1]:
                is_right = dfs(row, col+1, k+1, visited)

            if row > 0 and not visited[row-1][col]:
                is_top = dfs(row-1, col, k+1, visited)

            if row < height - 1 and not visited[row+1][col]:
                is_bottom = dfs(row+1, col, k+1, visited)

            visited[row][col] = False

            return is_left or is_right or is_top or is_bottom

        for i in range(height):
            for j in range(width):
                visited = [[False]*width for _ in range(height)]
                if dfs(i, j, 0, visited):
                    return True

        return False