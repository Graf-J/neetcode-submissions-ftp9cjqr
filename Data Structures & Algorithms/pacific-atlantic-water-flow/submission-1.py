class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        grid = [[[False, False] for _ in range(COLS)] for _ in range(ROWS)]
        q_pacific, q_atlantic = deque(), deque()
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    grid[r][c][0] = True
                    q_pacific.append((r, c))
                if r == ROWS - 1 or c == COLS - 1:
                    grid[r][c][1] = True
                    q_atlantic.append((r, c))

        while q_pacific:
            r, c = q_pacific.popleft()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if (
                    0 <= nr < ROWS and
                    0 <= nc < COLS and
                    grid[nr][nc][0] == False and
                    heights[nr][nc] >= heights[r][c]
                ):
                    grid[nr][nc][0] = True
                    q_pacific.append((nr, nc))

        while q_atlantic:
            r, c = q_atlantic.popleft()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if (
                    0 <= nr < ROWS and
                    0 <= nc < COLS and
                    grid[nr][nc][1] == False and
                    heights[nr][nc] >= heights[r][c]
                ):
                    grid[nr][nc][1] = True
                    q_atlantic.append((nr, nc))

        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if all(grid[r][c]):
                    result.append([r, c])

        return result



