class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pacific_reachable, atlantic_reachable = set(), set()
        q_pacific, q_atlantic = deque(), deque()
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    pacific_reachable.add((r, c))
                    q_pacific.append((r, c))
                if r == ROWS - 1 or c == COLS - 1:
                    atlantic_reachable.add((r, c))
                    q_atlantic.append((r, c))

        while q_pacific:
            r, c = q_pacific.popleft()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if (
                    0 <= nr < ROWS and
                    0 <= nc < COLS and
                    (nr, nc) not in pacific_reachable and
                    heights[nr][nc] >= heights[r][c]
                ):
                    pacific_reachable.add((nr, nc))
                    q_pacific.append((nr, nc))

        while q_atlantic:
            r, c = q_atlantic.popleft()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if (
                    0 <= nr < ROWS and
                    0 <= nc < COLS and
                    (nr, nc) not in atlantic_reachable and
                    heights[nr][nc] >= heights[r][c]
                ):
                    atlantic_reachable.add((nr, nc))
                    q_atlantic.append((nr, nc))

        result = pacific_reachable & atlantic_reachable
        return [[r, c] for r, c in result]



