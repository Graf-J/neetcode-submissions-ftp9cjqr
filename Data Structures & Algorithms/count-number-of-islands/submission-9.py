class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        def dfs(r, c):
            grid[r][c] = "0"
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if (
                    0 <= nr < ROW and
                    0 <= nc < COL and
                    grid[nr][nc] == "1"
                ):
                    dfs(nr, nc)

        num_islands = 0
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == "1":
                    num_islands += 1
                    dfs(row, col)

        return num_islands


