class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        min_heap = [(grid[0][0], 0, 0)]
        max_elevation = 0
        grid[0][0] = -1
        while min_heap:
            elevation, r, c = heapq.heappop(min_heap)
            max_elevation = max(max_elevation, elevation)
            if r == len(grid) - 1 and c == len(grid) - 1:
                break

            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if (
                    0 <= nr < len(grid) and
                    0 <= nc < len(grid) and
                    grid[nr][nc] >= 0
                ):
                    heapq.heappush(min_heap, (grid[nr][nc], nr, nc))
                    grid[nr][nc] = -1

        return max_elevation