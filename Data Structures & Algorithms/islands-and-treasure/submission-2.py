class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = (2 ** 31) - 1

        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r, c))

        distance = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if (
                        0 <= nr < len(grid) and
                        0 <= nc < len(grid[0]) and
                        grid[nr][nc] == INF
                    ):
                        grid[nr][nc] = distance
                        q.append((nr, nc))

            distance += 1