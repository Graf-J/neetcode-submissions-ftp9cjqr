class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row: int, col: int):
            grid[row][col] = "0"
            for nr, nc in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if (
                    0 <= nr < len(grid) and
                    0 <= nc < len(grid[0]) and
                    grid[nr][nc] == "1"
                ):
                    dfs(nr, nc)

        num_islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    num_islands += 1
                    dfs(r, c)

        return num_islands



# Time-Complexity: O(V + E)
# Space-Complexity: O(V)

            










