class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            stack = [(row, col)]
            grid[row][col] = "0"
            while stack:
                r, c = stack.pop()
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if (
                        0 <= nr < len(grid) and
                        0 <= nc < len(grid[0]) and
                        grid[nr][nc] == "1"
                    ):
                        grid[nr][nc] = "0"
                        stack.append((nr, nc))
            
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    dfs(row, col)
                    islands += 1

        return islands


