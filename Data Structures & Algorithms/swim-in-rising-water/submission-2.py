class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        visited = set()
        min_heap = [(grid[0][0], 0, 0)] # (elevation, row, col)
        min_time = 0

        while min_heap:
            elevation, r, c = heapq.heappop(min_heap)
            if (r, c) in visited:
                continue

            min_time = max(min_time, elevation)
            if r == ROW - 1 and c == COL - 1:
                break

            visited.add((r, c))
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if (
                    0 <= nr < ROW and
                    0 <= nc < COL and
                    (nr, nc) not in visited
                ):
                    heapq.heappush(min_heap, (grid[nr][nc], nr, nc))

        return min_time      









