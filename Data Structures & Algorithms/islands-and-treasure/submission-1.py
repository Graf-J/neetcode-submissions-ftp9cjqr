class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = (2**31) - 1
        ROW, COL = len(grid), len(grid[0])
        
        q = deque()
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 0:
                    q.append((row, col))

        distance = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if (
                        0 <= nr < ROW and
                        0 <= nc < COL and
                        grid[nr][nc] == inf
                    ):
                        grid[nr][nc] = distance
                        q.append((nr, nc))
            distance += 1

