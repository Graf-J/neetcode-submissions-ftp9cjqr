class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        max_elevation = grid[0][0]
        heap = [(grid[0][0], 0, 0)]
        grid[0][0] = -1

        while heap:
            elevation, r, c = heapq.heappop(heap)
            max_elevation = max(max_elevation, elevation)
            if r == ROWS - 1 and c == COLS - 1:
                break

            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if (
                    0 <= nr < ROWS and
                    0 <= nc < COLS and
                    grid[nr][nc] >= 0
                ):
                    heapq.heappush(heap, (grid[nr][nc], nr, nc))
                    grid[nr][nc] = -1

        return max_elevation
