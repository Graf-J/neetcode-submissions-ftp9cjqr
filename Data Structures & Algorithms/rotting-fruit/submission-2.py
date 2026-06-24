class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        
        num_fresh = 0
        q = deque()
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    num_fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        duration = 0
        while q and num_fresh:
            for _ in range(len(q)):
                r, c = q.popleft()
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if (
                        0 <= nr < ROW and
                        0 <= nc < COL and
                        grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        num_fresh -= 1

            duration += 1

        return duration if not num_fresh else -1

