class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])

        # Initialize with Borders
        pacific_set, atlantic_set = set(), set()
        pacific_stack, atlantic_stack = [], []
        for col in range(COL):
            pacific_stack.append((0, col))
            pacific_set.add((0, col))
            atlantic_stack.append((ROW - 1, col))
            atlantic_set.add((ROW - 1, col))
        for row in range(ROW):
            pacific_stack.append((row, 0))
            pacific_set.add((row, 0))
            atlantic_stack.append((row, COL - 1))
            atlantic_set.add((row, COL - 1))

        # Pacific DFS
        while pacific_stack:
            r, c = pacific_stack.pop()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if (
                    0 <= nr < ROW and
                    0 <= nc < COL and
                    (nr, nc) not in pacific_set and
                    heights[nr][nc] >= heights[r][c]
                ):
                    pacific_set.add((nr, nc))
                    pacific_stack.append((nr, nc))

        # Atlantic DFS
        while atlantic_stack:
            r, c = atlantic_stack.pop()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if (
                    0 <= nr < ROW and
                    0 <= nc < COL and
                    (nr, nc) not in atlantic_set and
                    heights[nr][nc] >= heights[r][c]
                ):
                    atlantic_set.add((nr, nc))
                    atlantic_stack.append((nr, nc))

        # Format Response
        return [[r, c] for r, c in (pacific_set & atlantic_set)]


        