class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = {}
        def dfs(r: int, c: int) -> int:
            if (r, c) in memo:
                return memo[(r, c)]

            result = 1
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if (
                    0 <= nr < m and
                    0 <= nc < n and
                    matrix[nr][nc] > matrix[r][c]
                ):
                    result = max(result, 1 + dfs(nr, nc))

            memo[(r, c)] = result
            return result

        return max(dfs(i, j) for i in range(m) for j in range(n))