# Multi-Start BFS
# Elegant making of visited nodes in-place
# Elegant way to avoid BFS grouping (increment by one relative to previous)

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if (
                    0 <= nr < len(grid) and
                    0 <= nc < len(grid[0]) and
                    grid[nr][nc] == (2 ** 31 - 1)
                ):
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
