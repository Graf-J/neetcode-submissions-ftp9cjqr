class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        diameter = 0
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    continue
                    
                diameter += 4
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if (
                        0 <= nr < len(grid) and
                        0 <= nc < len(grid[0]) and
                        (nr, nc) in visited
                    ):
                        diameter -= 2
                visited.add((r, c))

        return diameter







