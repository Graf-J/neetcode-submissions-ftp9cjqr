class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        rotten_fruits = 0
        total_fruits = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] > 0:
                    total_fruits += 1
                if grid[r][c] == 2:
                    rotten_fruits += 1
                    q.append((r, c))


        minutes = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        rotten_fruits += 1
                        q.append((nr, nc))

            minutes += 1

        return max(0, minutes - 1) if rotten_fruits == total_fruits else -1

# minutes = 5
# q = []

# [2,2,0]
# [0,2,2]
# [0,2,2]



