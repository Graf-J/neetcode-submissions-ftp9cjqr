class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(r, c):
            q = deque([(r, c)])
            while q:
                r, c = q.popleft()
                grid[r][c] = "0"

                positions = ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1))
                for r_new, c_new in positions:
                    if (
                        0 <= r_new < len(grid) and
                        0 <= c_new < len(grid[0]) and
                        grid[r_new][c_new] == "1"
                    ):
                        q.append((r_new, c_new))

        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    bfs(row, col)
                    islands += 1
        
        return islands