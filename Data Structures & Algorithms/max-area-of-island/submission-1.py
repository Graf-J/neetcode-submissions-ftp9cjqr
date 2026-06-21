class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        def dfs(r, c) -> int:
            if (
                r < 0 or r == ROW or
                c < 0 or c == COL or
                grid[r][c] == 0
            ):
                return 0

            grid[r][c] = 0
            return (
                1 +
                dfs(r + 1, c) + 
                dfs(r - 1, c) + 
                dfs(r, c + 1) +
                dfs(r, c - 1)
            )

        max_area = 0
        for row in range(ROW):
            for col in range(COL):
                max_area = max(max_area, dfs(row, col))

        return max_area




