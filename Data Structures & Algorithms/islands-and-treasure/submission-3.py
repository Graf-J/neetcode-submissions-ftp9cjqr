class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS, INF = len(grid), len(grid[0]), (2**31) - 1

        q = deque((r, c) for r in range(ROWS) for c in range(COLS) if grid[r][c] == 0)

        dist = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        grid[nr][nc] == INF
                    ):
                        grid[nr][nc] = dist
                        q.append((nr, nc))
            dist += 1

