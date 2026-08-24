class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> int:
            grid[r][c] = 0
            neighbour_size = 1
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if (
                    0 <= nr < ROWS and
                    0 <= nc < COLS and
                    grid[nr][nc]
                ):
                    neighbour_size += dfs(nr, nc)

            return neighbour_size

        max_area = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    area = dfs(i, j)
                    max_area = max(max_area, area)

        return max_area
