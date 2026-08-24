class Solution:
    def erase_island(self, grid, row, col):
        ROWS, COLS = len(grid), len(grid[0])
        
        stack = [(row, col)]
        grid[row][col] = "0"
        while stack:
            r, c = stack.pop()
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if (
                    0 <= nr < ROWS and
                    0 <= nc < COLS and
                    grid[nr][nc] == "1"
                ):
                    grid[nr][nc] = "0"
                    stack.append((nr, nc))


    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        num_islands = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    num_islands += 1
                    self.erase_island(grid, i, j)

        return num_islands

            










