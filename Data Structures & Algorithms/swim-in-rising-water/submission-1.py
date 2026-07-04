class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        max_elevation = 0
        min_heap = [(0, 0, 0)]
        while min_heap:
            elevation, r, c = heapq.heappop(min_heap)
            if grid[r][c] == -1:
                continue

            max_elevation = max(max_elevation, grid[r][c])
            grid[r][c] = -1
            if r == n - 1 and c == n - 1:
                break

            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if (
                    0 <= nr < n and
                    0 <= nc < n and
                    grid[nr][nc] != -1
                ):
                    heapq.heappush(min_heap, (grid[nr][nc], nr, nc))

        return max_elevation
                