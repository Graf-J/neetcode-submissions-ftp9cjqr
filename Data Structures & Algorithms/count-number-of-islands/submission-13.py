class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> int:
            if (
                r < 0 or r == ROWS or
                c < 0 or c == COLS or
                grid[r][c] == "0"
            ):
                return

            grid[r][c] = "0"
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                dfs(nr, nc)

        result = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    result += 1
                    dfs(row, col)

        return result

