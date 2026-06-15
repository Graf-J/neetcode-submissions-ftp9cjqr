# Elegant Visited (no explicit set but inplace)
# DFS / BFS (regular with stack / queue)
# BFS with grouping

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            area = 1
            stack = [(row, col)]
            grid[row][col] = 0
            while stack:
                r, c = stack.pop()
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if (
                        0 <= nr < len(grid) and
                        0 <= nc < len(grid[0]) and
                        grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 0
                        stack.append((nr, nc))
                        area += 1
            return area

        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))

        return max_area
            
