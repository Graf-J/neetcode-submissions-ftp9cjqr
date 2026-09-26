class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])

        atlantic_visited, pacific_visited = set(), set()

        def dfs(r: int, c: int, parent_val: int, visited: set[tuple[int, int]]) -> None:
            if (
                r < 0 or r >= ROW or
                c < 0 or c >= COL or
                heights[r][c] < parent_val or
                (r, c) in visited
            ):
                return

            visited.add((r, c))
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                dfs(nr, nc, heights[r][c], visited)

        for c in range(COL):
            dfs(0, c, heights[0][c], pacific_visited)
            dfs(ROW - 1, c, heights[ROW - 1][c], atlantic_visited)

        for r in range(ROW):
            dfs(r, 0, heights[r][0], pacific_visited)
            dfs(r, COL - 1, heights[r][COL - 1], atlantic_visited)


        return list(atlantic_visited & pacific_visited)