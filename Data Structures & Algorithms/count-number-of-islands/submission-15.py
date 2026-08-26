class Solution:
    def numIslands(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r: int, c: int) -> int:
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if (
                    0 <= nr < ROWS and
                    0 <= nc < COLS and
                    grid[nr][nc] == "1"
                ):
                    grid[nr][nc] = "0"
                    dfs(nr, nc)

        num_islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    dfs(r, c)
                    num_islands += 1

        return num_islands

            










